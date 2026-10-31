# tests

Preservação Unicode, homógrafos, exportação e métricas.

Conteúdo: `test_tupi.py` e `test_legado_recuperado.py`, totalizando 12 testes. O segundo caracteriza as regras recuperadas e garante que o importador padrão continua conservador.

Leia o [guia principal](../README.md), os [contratos](../docs/ARQUITETURA.md) e a [procedência](../docs/PROCEDENCIA.md). Execute conforme [INSTALACAO.md](../docs/INSTALACAO.md).

Para estudar: identifique entrada e saída, acompanhe um exemplo pequeno e investigue um caso de fronteira. As conclusões e limites estão em [VALIDACAO.md](../docs/VALIDACAO.md).

O núcleo do acervo recuperado tem teste separado em `scripts/verificar_colab_recuperado.py`. As células interativas de Colab não são executadas pela suíte. Um teste aprovado não valida todas as entradas possíveis nem equivale à avaliação institucional da entrega original.
