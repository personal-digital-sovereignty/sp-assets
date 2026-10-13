# Linha `treesitter-grammars` — gramáticas tree-sitter compiladas para `.wasm`

Gramáticas [tree-sitter](https://tree-sitter.github.io/) compiladas para WebAssembly (`dylink.0`), carregadas em runtime pelo catálogo do RAG do Coding do Sovereign Pair (`tree_sitter::WasmStore` + `wasmtime`). Nunca são compiladas dentro do binário do produto.

| Release | Publicada | Assets |
|---|---|---|
| [`treesitter-grammars-v1`](https://github.com/personal-digital-sovereignty/sp-assets/releases/tag/treesitter-grammars-v1) | 2026-08-28 | 23 `.wasm` + `THIRD_PARTY_NOTICES.md` |

## Proveniência de cada artefato

Fonte de verdade legível por máquina: [`proveniencia.json`](proveniencia.json). Textos de licença copiados do commit exato: [`licencas/`](licencas/).

| Asset | Origem (no commit) | Commit | Licença | Lote |
|---|---|---|---|---|
| `tree-sitter-bash.wasm` | [tree-sitter/tree-sitter-bash](https://github.com/tree-sitter/tree-sitter-bash/tree/a06c2e4415e9bc0346c6b86d401879ffb44058f7) | `a06c2e4415e9` | MIT | 2 |
| `tree-sitter-c.wasm` | [tree-sitter/tree-sitter-c](https://github.com/tree-sitter/tree-sitter-c/tree/b780e47fc780ddc8da13afa35a3f4ed5c157823d) | `b780e47fc780` | MIT | 2 |
| `tree-sitter-c_sharp.wasm` | [tree-sitter/tree-sitter-c-sharp](https://github.com/tree-sitter/tree-sitter-c-sharp/tree/9150f7d56bb47f1a809fa23623f1ba1413e93fa9) | `9150f7d56bb4` | MIT | 2 |
| `tree-sitter-cpp.wasm` | [tree-sitter/tree-sitter-cpp](https://github.com/tree-sitter/tree-sitter-cpp/tree/8b5b49eb196bec7040441bee33b2c9a4838d6967) | `8b5b49eb196b` | MIT | 2 |
| `tree-sitter-dart.wasm` | [UserNobody14/tree-sitter-dart](https://github.com/UserNobody14/tree-sitter-dart/tree/be07cf7118d3dba06236a3f19541685a68209934) | `be07cf7118d3` | MIT | 2 |
| `tree-sitter-elixir.wasm` | [elixir-lang/tree-sitter-elixir](https://github.com/elixir-lang/tree-sitter-elixir/tree/4b0c7118760af58a2e7081bbc8396e136f820b37) | `4b0c7118760a` | Apache-2.0 | 2 |
| `tree-sitter-go.wasm` | [tree-sitter/tree-sitter-go](https://github.com/tree-sitter/tree-sitter-go/tree/2346a3ab1bb3857b48b29d779a1ef9799a248cd7) | `2346a3ab1bb3` | MIT | 2 |
| `tree-sitter-haskell.wasm` | [tree-sitter/tree-sitter-haskell](https://github.com/tree-sitter/tree-sitter-haskell/tree/0975ef72fc3c47b530309ca93937d7d143523628) | `0975ef72fc3c` | MIT | 2 |
| `tree-sitter-java.wasm` | [tree-sitter/tree-sitter-java](https://github.com/tree-sitter/tree-sitter-java/tree/e10607b45ff745f5f876bfa3e94fbcc6b44bdc11) | `e10607b45ff7` | MIT | 2 |
| `tree-sitter-javascript.wasm` | [tree-sitter/tree-sitter-javascript](https://github.com/tree-sitter/tree-sitter-javascript/tree/58404d8cf191d69f2674a8fd507bd5776f46cb11) | `58404d8cf191` | MIT | 1 |
| `tree-sitter-json.wasm` | [tree-sitter/tree-sitter-json](https://github.com/tree-sitter/tree-sitter-json/tree/254c42a6476413b776221e03982ac8ae159eeb72) | `254c42a64764` | MIT | 1 |
| `tree-sitter-kotlin.wasm` | [fwcd/tree-sitter-kotlin](https://github.com/fwcd/tree-sitter-kotlin/tree/1852ea17b7f60fb3f9d84e0b1555d56b46b39fb1) | `1852ea17b7f6` | MIT | 2 |
| `tree-sitter-lua.wasm` | [tree-sitter-grammars/tree-sitter-lua](https://github.com/tree-sitter-grammars/tree-sitter-lua/tree/10fe0054734eec83049514ea2e718b2a56acd0c9) | `10fe0054734e` | MIT | 2 |
| `tree-sitter-php.wasm` | [tree-sitter/tree-sitter-php](https://github.com/tree-sitter/tree-sitter-php/tree/3fda2fb9577166c6399834917f9844f30370beea) `php/` | `3fda2fb95771` | MIT | 2 |
| `tree-sitter-python.wasm` | [tree-sitter/tree-sitter-python](https://github.com/tree-sitter/tree-sitter-python/tree/26855eabccb19c6abf499fbc5b8dc7cc9ab8bc64) | `26855eabccb1` | MIT | 1 |
| `tree-sitter-r.wasm` | [r-lib/tree-sitter-r](https://github.com/r-lib/tree-sitter-r/tree/58a22794466c0fc15b0d3b40531db751593721e8) | `58a22794466c` | MIT | 2 |
| `tree-sitter-ruby.wasm` | [tree-sitter/tree-sitter-ruby](https://github.com/tree-sitter/tree-sitter-ruby/tree/ad907a69da0c8a4f7a943a7fe012712208da6dee) | `ad907a69da0c` | MIT | 2 |
| `tree-sitter-rust.wasm` | [tree-sitter/tree-sitter-rust](https://github.com/tree-sitter/tree-sitter-rust/tree/77a3747266f4d621d0757825e6b11edcbf991ca5) | `77a3747266f4` | MIT | 1 |
| `tree-sitter-scala.wasm` | [tree-sitter/tree-sitter-scala](https://github.com/tree-sitter/tree-sitter-scala/tree/db390f312a54b04b13790e1767bfac32665c17ac) | `db390f312a54` | MIT | 2 |
| `tree-sitter-swift.wasm` | [alex-pinkus/tree-sitter-swift](https://github.com/alex-pinkus/tree-sitter-swift/tree/45e8dcdf09d67e63b6e1f7d47e9ac7d123a34269) | `45e8dcdf09d6` | MIT | 2 |
| `tree-sitter-tsx.wasm` | [tree-sitter/tree-sitter-typescript](https://github.com/tree-sitter/tree-sitter-typescript/tree/75b3874edb2dc714fb1fd77a32013d0f8699989f) `tsx/` | `75b3874edb2d` | MIT | 1 |
| `tree-sitter-typescript.wasm` | [tree-sitter/tree-sitter-typescript](https://github.com/tree-sitter/tree-sitter-typescript/tree/75b3874edb2dc714fb1fd77a32013d0f8699989f) `typescript/` | `75b3874edb2d` | MIT | 1 |
| `tree-sitter-yaml.wasm` | [tree-sitter-grammars/tree-sitter-yaml](https://github.com/tree-sitter-grammars/tree-sitter-yaml/tree/a1c4812a73ec5e089de8e441fdea3a921e8d5079) | `a1c4812a73ec` | MIT | 1 |

**Como a proveniência foi provada (2026-10-13).** As notas originais da release listavam só 7 das 23 gramáticas e não registravam commit: o build fazia clone raso do branch padrão. Os commits foram recuperados e **provados por SHA-256**:

- **Lote 2** (16 gramáticas, publicadas às 16:17 UTC): os clones usados no build ainda existiam; o binário gerado deles é idêntico ao publicado.
- **Lote 1** (7 gramáticas, publicadas às 10:39 UTC): commit reconstruído como o último do branch padrão antes do upload, recompilado de forma independente com o mesmo `tree-sitter-cli` 0.26.13 e o mesmo processo da época (`build --wasm` sobre o `parser.c` commitado, sem `generate`) — os 7 SHA-256 batem. A primeira tentativa, com `generate`, não bateu em 6 de 7: o processo também faz parte da proveniência.

Os mesmos SHA-256 estão fixados no consumidor (`sp-service/src/code_grammars.rs`), que confere cada download.

## Processo de build

| Lote | Script (no `sp-service`) | Comandos |
|---|---|---|
| 1 | `711ffea:scripts/build_treesitter_grammars.sh` | `git clone --depth 1` → `tree-sitter build --wasm` |
| 2 | `5cbfbe8:scripts/build_treesitter_grammars.sh` | `git clone --depth 1` → `tree-sitter generate` → `tree-sitter build --wasm` |

Ferramenta: `tree-sitter-cli` 0.26.13 (MIT), que não é redistribuída. Conferido nos binários: eles **importam** a libc do hospedeiro (`malloc`, `iswalnum`, …) em vez de embuti-la, então cada `.wasm` contém o código da própria gramática — daí os avisos serem as licenças dos upstreams.

## Licenças

22 gramáticas são MIT, cada uma com o próprio aviso de copyright; `tree-sitter-elixir` é **Apache-2.0** e o `NOTICE` dele é redistribuído junto. Tudo reproduzido em [`../THIRD_PARTY_NOTICES.md`](../THIRD_PARTY_NOTICES.md), também anexado à release.

**Registro de falha.** A release `treesitter-grammars-v1` foi publicada em 2026-08-28 sem os avisos de copyright e sem a licença Apache-2.0/`NOTICE` exigidos pelos autores. Corrigido em 2026-10-13: avisos anexados à release, proveniência completa neste diretório e verificação automática na CI para que nenhum artefato volte a sair sem eles.
