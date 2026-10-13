# sp-assets

Distribuição pública de artefatos binários do [Sovereign Pair](https://github.com/personal-digital-sovereignty). O que está aqui é baixado em runtime pelo produto, sem autenticação — por isso o repositório é público.

**Regra do repositório: nenhum artefato sai daqui sem a licença e o aviso da sua origem.** Cada asset de cada release tem proveniência (repositório e commit exatos), licença do autor e texto da licença copiado daquele commit. A CI (`.github/workflows/avisos.yml`) reprova o que não cumprir isso.

## Linhas de release

Cada linha tem um diretório de documentação, um manifesto de proveniência e um prefixo de tag próprio. Uma linha não compartilha tag nem notas com outra.

| Linha | Tag | Documentação | Consumidor | Licenças de terceiros |
|---|---|---|---|---|
| Gramáticas tree-sitter (`.wasm`) | `treesitter-grammars-vN` | [`treesitter-grammars/`](treesitter-grammars/README.md) | catálogo do RAG do Coding (`sp-service`) | 22 MIT, 1 Apache-2.0 |

**Contrato**: as URLs `releases/download/<tag>/<arquivo>` estão compiladas em versões já distribuídas do produto. Tag publicada não se renomeia, não se apaga e não tem asset substituído; mudança vira tag nova (`-v2`). Anexar documentos (como `THIRD_PARTY_NOTICES.md`) a uma release existente é permitido — não muda nenhuma URL de artefato.

## Licenças

- **Conteúdo próprio** (documentação, manifestos e scripts): MIT — ver [`LICENSE`](LICENSE).
- **Artefatos das releases**: compilados de código de terceiros; continuam sob a licença de cada autor — ver [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md), também anexado a cada release. A licença MIT deste repositório não relicencia nada de terceiros.

## Publicar uma release nova (ou um asset novo)

1. Compile registrando o **commit exato** de cada upstream (o script de build fica no repositório do consumidor).
2. Acrescente o asset ao `<linha>/proveniencia.json`: arquivo, SHA-256, upstream, commit (40 caracteres), licença SPDX e os arquivos de licença copiados **daquele commit** para `<linha>/licencas/`. Licença fora da lista revisada em `scripts/avisos.py` exige revisão humana antes.
3. `python3 scripts/avisos.py gerar` e `python3 scripts/avisos.py verificar`.
4. PR; a CI tem de passar.
5. Publique a release com os assets **e** o `THIRD_PARTY_NOTICES.md` anexado; a CI roda de novo no evento da release (`verificar-releases`).

## Verificação local

```bash
python3 -m unittest discover -s scripts -p 'test_*.py'
python3 scripts/avisos.py verificar
python3 scripts/avisos.py verificar-releases
```
