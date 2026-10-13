#!/usr/bin/env python3
"""Avisos de terceiros do sp-assets: gerar e verificar.

Regra do repositório: **nenhum artefato sai daqui sem a licença e o aviso da sua
origem.** Cada linha de release tem um manifesto (`<linha>/proveniencia.json`)
que diz, para cada asset: repositório de origem, commit exato, licença (SPDX) e
os arquivos de licença copiados DAQUELE commit. O `THIRD_PARTY_NOTICES.md` da
raiz é gerado desses manifestos — nunca editado à mão.

    python3 scripts/avisos.py gerar              # reescreve THIRD_PARTY_NOTICES.md
    python3 scripts/avisos.py verificar          # offline: manifestos, textos e avisos em sincronia
    python3 scripts/avisos.py verificar-releases # online: todo asset publicado tem proveniência e SHA igual

`verificar-releases` usa a API pública do GitHub (GITHUB_TOKEN opcional, só para
limite de taxa). Sai com 1 em qualquer divergência — fail-loud.

Somente biblioteca padrão.
"""
from __future__ import annotations

import json
import os
import sys
import urllib.request
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
AVISOS = RAIZ / "THIRD_PARTY_NOTICES.md"
REPO = os.environ.get("SP_ASSETS_REPO", "personal-digital-sovereignty/sp-assets")

# Licenças aceitas para redistribuição aqui. Licença nova exige revisão humana:
# entra nesta lista num commit próprio, dizendo o que ela obriga.
PERMITIDAS = {"MIT", "Apache-2.0", "BSD-2-Clause", "BSD-3-Clause", "ISC", "Zlib"}
# Licenças cujo texto exige redistribuir o NOTICE do upstream quando ele existe.
EXIGEM_NOTICE = {"Apache-2.0"}
ANEXO = "THIRD_PARTY_NOTICES.md"


def manifestos() -> list[tuple[Path, dict]]:
    return [(p, json.loads(p.read_text("utf-8"))) for p in sorted(RAIZ.glob("*/proveniencia.json"))]


def gerar_texto() -> str:
    linhas = [
        "# Avisos de terceiros (THIRD-PARTY NOTICES)",
        "",
        "> **Gerado** por `scripts/avisos.py gerar` a partir de `*/proveniencia.json`. Não edite à mão.",
        ">",
        "> Os artefatos binários publicados nas releases deste repositório são compilados de código de terceiros.",
        "> Cada um continua sob a licença do seu autor, reproduzida abaixo **a partir do commit exato** de onde",
        "> foi compilado. A licença MIT da raiz (`LICENSE`) cobre só o conteúdo próprio deste repositório",
        "> (documentação e scripts) — não relicencia nada de terceiros.",
        "",
    ]
    for _, m in manifestos():
        linhas += [f"## Linha `{m['linha']}` — release `{m['release']}`", ""]
        linhas += ["| Asset | Origem | Commit | Licença |", "|---|---|---|---|"]
        for a in m["assets"]:
            linhas.append(f"| `{a['arquivo']}` | {a['upstream']} | `{a['commit'][:12]}` | {a['licenca_spdx']} |")
        linhas.append("")
        grupos: dict[str, list[str]] = {}
        for a in m["assets"]:
            grupos.setdefault(a["upstream"] + "@" + a["commit"], []).append(a["arquivo"])
        for a in m["assets"]:
            chave = a["upstream"] + "@" + a["commit"]
            if chave not in grupos:
                continue
            arquivos = grupos.pop(chave)
            sub = f" (subdiretório `{a['subdiretorio']}`)" if a.get("subdiretorio") else ""
            linhas += [
                f"### {a['upstream'].split('github.com/')[-1]} — {a['licenca_spdx']}",
                "",
                f"- Usado em: {', '.join(f'`{x}`' for x in arquivos)}",
                f"- Origem: {a['upstream']}/tree/{a['commit']}{sub}",
                "",
            ]
            for rel in a["arquivos_de_licenca"]:
                texto = (RAIZ / rel).read_text("utf-8").rstrip("\n")
                linhas += [f"#### `{Path(rel).name}`", "", "```text", texto, "```", ""]
    return "\n".join(linhas).rstrip("\n") + "\n"


def verificar() -> list[str]:
    erros: list[str] = []
    ms = manifestos()
    if not ms:
        erros.append("nenhum */proveniencia.json encontrado")
    for caminho, m in ms:
        nomes: set[str] = set()
        for a in m.get("assets", []):
            onde = f"{caminho.relative_to(RAIZ)}:{a.get('arquivo', '?')}"
            for campo in ("arquivo", "sha256", "upstream", "commit", "licenca_spdx", "arquivos_de_licenca"):
                if not a.get(campo):
                    erros.append(f"{onde}: campo obrigatório ausente: {campo}")
            if a.get("arquivo") in nomes:
                erros.append(f"{onde}: asset duplicado no manifesto")
            nomes.add(a.get("arquivo", ""))
            if len(a.get("commit", "")) != 40:
                erros.append(f"{onde}: commit precisa ser o SHA completo (40 caracteres)")
            if len(a.get("sha256", "")) != 64:
                erros.append(f"{onde}: sha256 precisa ter 64 caracteres hexadecimais")
            if a.get("licenca_spdx") not in PERMITIDAS:
                erros.append(f"{onde}: licença {a.get('licenca_spdx')!r} fora da lista revisada {sorted(PERMITIDAS)}")
            arquivos = a.get("arquivos_de_licenca") or []
            if not any(Path(x).name.upper().startswith(("LICENSE", "LICENCE", "COPYING")) for x in arquivos):
                erros.append(f"{onde}: sem texto de licença")
            if a.get("licenca_spdx") in EXIGEM_NOTICE and a.get("notice_upstream", True) \
                    and not any(Path(x).name.upper().startswith("NOTICE") for x in arquivos):
                erros.append(f"{onde}: {a['licenca_spdx']} exige redistribuir o NOTICE do upstream "
                             "(se o upstream não tem NOTICE, declare \"notice_upstream\": false)")
            for rel in arquivos:
                p = RAIZ / rel
                if not p.is_file() or not p.read_text("utf-8", errors="replace").strip():
                    erros.append(f"{onde}: arquivo de licença ausente ou vazio: {rel}")
    if not AVISOS.exists():
        erros.append(f"{ANEXO} ausente — rode: python3 scripts/avisos.py gerar")
    elif not erros and AVISOS.read_text("utf-8") != gerar_texto():
        erros.append(f"{ANEXO} desatualizado — rode: python3 scripts/avisos.py gerar")
    return erros


def _api(url: str):
    req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json"})
    tok = os.environ.get("GITHUB_TOKEN")
    if tok:
        req.add_header("Authorization", f"Bearer {tok}")
    with urllib.request.urlopen(req, timeout=30) as r:  # nosemgrep
        return json.load(r)


def verificar_releases() -> list[str]:
    erros: list[str] = []
    por_release = {m["release"]: {a["arquivo"]: a for a in m["assets"]} for _, m in manifestos()}
    for rel in _api(f"https://api.github.com/repos/{REPO}/releases?per_page=100"):
        tag = rel["tag_name"]
        esperados = por_release.get(tag)
        if esperados is None:
            erros.append(f"release {tag}: sem manifesto de proveniência (*/proveniencia.json)")
            continue
        publicados: set[str] = set()
        for asset in rel.get("assets", []):
            nome = asset["name"]
            publicados.add(nome)
            if nome == ANEXO:
                continue
            m = esperados.get(nome)
            if m is None:
                erros.append(f"release {tag}: asset {nome} sem proveniência no manifesto")
                continue
            digest = (asset.get("digest") or "").removeprefix("sha256:")
            if not digest:
                erros.append(f"release {tag}: {nome} sem digest na API — confira o SHA-256 baixando o arquivo")
            elif digest != m["sha256"]:
                erros.append(f"release {tag}: {nome} com SHA-256 diferente do manifesto")
        for nome in esperados:
            if nome not in publicados:
                erros.append(f"release {tag}: manifesto cita {nome}, que não está publicado")
        if ANEXO not in publicados:
            erros.append(f"release {tag}: {ANEXO} não está anexado à release")
    return erros


def main(argv: list[str]) -> int:
    cmd = argv[0] if argv else ""
    if cmd == "gerar":
        AVISOS.write_text(gerar_texto(), "utf-8")
        print(f"gerado: {ANEXO}")
        return 0
    if cmd in ("verificar", "verificar-releases"):
        erros = verificar() if cmd == "verificar" else verificar_releases()
        for e in erros:
            print(f"❌ {e}")
        if erros:
            return 1
        print(f"✅ {cmd}: em ordem")
        return 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
