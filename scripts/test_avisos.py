"""Prova que o verificador de avisos reprova o que tem de reprovar.

Cada teste copia o repositório para um diretório temporário, planta um defeito e
exige que `avisos.py verificar` saia com 1. Sem isso, o verificador seria só um
script que imprime ✅.

    python3 -m unittest discover -s scripts -p 'test_*.py'
"""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]


class Verificador(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.r = Path(self._tmp.name) / "repo"
        shutil.copytree(RAIZ, self.r, ignore=shutil.ignore_patterns(".git", "__pycache__"))

    def tearDown(self):
        self._tmp.cleanup()

    def rodar(self) -> subprocess.CompletedProcess:
        return subprocess.run([sys.executable, str(self.r / "scripts" / "avisos.py"), "verificar"],
                              capture_output=True, text=True)

    def manifesto(self) -> Path:
        return self.r / "treesitter-grammars" / "proveniencia.json"

    def mutar(self, f):
        d = json.loads(self.manifesto().read_text("utf-8"))
        f(d)
        self.manifesto().write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", "utf-8")

    def test_estado_atual_passa(self):
        r = self.rodar()
        self.assertEqual(r.returncode, 0, r.stdout)

    def test_apache_sem_notice_reprova(self):
        def f(d):
            for a in d["assets"]:
                if a["licenca_spdx"] == "Apache-2.0":
                    a["arquivos_de_licenca"] = [x for x in a["arquivos_de_licenca"] if not x.endswith("NOTICE")]
        self.mutar(f)
        r = self.rodar()
        self.assertEqual(r.returncode, 1)
        self.assertIn("exige redistribuir o NOTICE", r.stdout)

    def test_licenca_fora_da_lista_reprova(self):
        self.mutar(lambda d: d["assets"][0].update(licenca_spdx="GPL-3.0-only"))
        r = self.rodar()
        self.assertEqual(r.returncode, 1)
        self.assertIn("fora da lista revisada", r.stdout)

    def test_sem_texto_de_licenca_reprova(self):
        self.mutar(lambda d: d["assets"][0].update(arquivos_de_licenca=[]))
        self.assertEqual(self.rodar().returncode, 1)

    def test_texto_de_licenca_apagado_reprova(self):
        alvo = next((self.r / "treesitter-grammars" / "licencas").rglob("LICENSE*"))
        alvo.write_text("", "utf-8")
        r = self.rodar()
        self.assertEqual(r.returncode, 1)
        self.assertIn("ausente ou vazio", r.stdout)

    def test_commit_abreviado_reprova(self):
        self.mutar(lambda d: d["assets"][0].update(commit=d["assets"][0]["commit"][:12]))
        self.assertEqual(self.rodar().returncode, 1)

    def test_aviso_editado_a_mao_reprova(self):
        p = self.r / "THIRD_PARTY_NOTICES.md"
        p.write_text(p.read_text("utf-8") + "\nlinha editada à mão\n", "utf-8")
        r = self.rodar()
        self.assertEqual(r.returncode, 1)
        self.assertIn("desatualizado", r.stdout)


if __name__ == "__main__":
    unittest.main()
