# sp-assets

Distribuição de artefatos binários públicos do Sovereign Pair (gramáticas `tree-sitter` pro RAG do Coding, e potencialmente outros catálogos públicos no futuro).

**Este repositório não contém código-fonte** — a fonte real do projeto vive nos repos privados (`sp-service`, `sp-ui-*`). Aqui só ficam releases com artefatos binários buildados por nós, com proveniência documentada em cada release, pra distribuição pública sem exigir autenticação (diferente de assets em repo privado, que exigiriam token).

## Releases

- [`treesitter-grammars-v1`](https://github.com/personal-digital-sovereignty/sp-assets/releases/tag/treesitter-grammars-v1) — gramáticas `tree-sitter` (`.wasm`) pro chunking AST-aware do RAG do Coding ([ADR-020](https://github.com/personal-digital-sovereignty/sp-service) do `sp-service`). Buildadas via `sp-service/scripts/build_treesitter_grammars.sh`, código-fonte de cada gramática é o repositório oficial de cada linguagem (ver notas da release).
