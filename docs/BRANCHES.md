# Branches e entregas

Use `main` para clonar e executar a versão consolidada. As branches abaixo preservam o ponto de entrega de cada assunto; depois da integração, podem estar atrás de `main`.

Cada branch está ligada a uma alteração concreta. A organização foi feita nesta edição: os nomes não indicam trabalho em datas antigas nem revisão de outras pessoas.

| Branch | Finalidade | Acesso |
| --- | --- | --- |
| `main` | Código e documentação consolidados | [Abrir](https://github.com/luigiscofano/ic-pln-tupi-antigo/tree/main) |
| `docs/parceria-calebe-rezende` | Referenciar o projeto de Calebe Rezende, a parceria e os créditos | [PR #9](https://github.com/luigiscofano/ic-pln-tupi-antigo/pull/9) · [Guia](PARCERIAS.md) |
| `docs/evidencia-da-ci` | Registrar validacao remota e artefatos reproduziveis | [PR #5](https://github.com/luigiscofano/ic-pln-tupi-antigo/pull/5) |
| `docs/guia-das-ferramentas-novas` | Documentar ferramentas novas e objetivos pedagogicos | [PR #4](https://github.com/luigiscofano/ic-pln-tupi-antigo/pull/4) |
| `feat/demonstracao-sintetica` | Adicionar demonstracao sintetica e adaptador OCR opcional | [PR #2](https://github.com/luigiscofano/ic-pln-tupi-antigo/pull/2) |
| `feat/fundamentos` | Implementar preservacao Unicode e auditoria lexicografica | [PR #1](https://github.com/luigiscofano/ic-pln-tupi-antigo/pull/1) |
| `test/verificacao-automatica` | Adicionar testes executaveis e GitHub Actions | [PR #3](https://github.com/luigiscofano/ic-pln-tupi-antigo/pull/3) |
| `acervo/colab-recuperado` | Publicar Colab recuperado com guia de execução | [Guia](../docs/topicos/ACERVO_COLAB.md) · [Branch](https://github.com/luigiscofano/ic-pln-tupi-antigo/tree/acervo/colab-recuperado) |
| `feat/heuristicas-ortograficas` | Publicar regras recuperadas e testar transformação XLSX/CSV | [Guia](../docs/topicos/HEURISTICAS.md) · [Branch](https://github.com/luigiscofano/ic-pln-tupi-antigo/tree/feat/heuristicas-ortograficas) |
| `docs/pesquisa-e-evidencias` | Publicar documentação autorizada da pesquisa e diário | [Guia](../docs/topicos/PESQUISA.md) · [Branch](https://github.com/luigiscofano/ic-pln-tupi-antigo/tree/docs/pesquisa-e-evidencias) |

## Como continuar

Parta da versão atual de `main`, crie uma branch para uma mudança delimitada e abra um PR explicando comportamento, motivo e validação. Não use branches antigas como base para novos assuntos sem atualizar a base.

```sh
git switch main
git pull --ff-only
git switch -c docs/nova-atividade
```

[Guias por assunto](topicos/README.md) · [Registro de publicação](PUBLICACAO.md) · [Todos os PRs](https://github.com/luigiscofano/ic-pln-tupi-antigo/pulls?q=is%3Apr)
