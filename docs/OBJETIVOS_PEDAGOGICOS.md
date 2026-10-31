# Objetivos pedagógicos

**A meta é explicar o mecanismo e demonstrar o resultado.** Cada atividade exige evidência observável.

| Competência | Atividade | Evidência de aprendizagem |
| --- | --- | --- |
| Separar fonte e interpretação | Manter lemma_raw e cópia NFC | Provar que a forma decomposta não foi substituída |
| Tratar ausência sem inventar | Manter tradução vazia | Exibir missing_en sem preencher por analogia |
| Preservar homógrafos | Manter IDs distintos para lema igual | Explicar por que repetição não implica erro |
| Avaliar OCR | Calcular CER/WER em pares alinhados | Distinguir fixture de benchmark com revisão humana |
| Distinguir tipos de validação | Executar a suíte de software | Explicar por que aprovação funcional não demonstra correção linguística |
| Documentar revisão | Manter status pending_review | Exigir decisão documentada para promover um registro |

## Sequência de estudo

1. Leia o contrato e resolva um exemplo pequeno à mão.
2. Preveja saída e estado intermediário antes de executar.
3. Confronte sua previsão com o programa.
4. Altere uma entrada de fronteira e justifique o resultado.
5. Explique o invariante violado em um teste negativo.
6. Proponha uma extensão com critério de aceitação.

## Rubrica sugerida

| Critério | Inicial | Adequado | Avançado |
| --- | --- | --- | --- |
| Explicação | Repete a saída | Explica etapas | Justifica invariante e contraexemplo |
| Verificação | Usa um exemplo | Testa fronteiras | Compara com referência independente |
| Limites | Omite hipóteses | Declara domínio | Explica falha e sua detecção |
| Reprodução | Depende do ambiente pessoal | Usa comandos e fixtures | Registra versão, origem e evidência |

Rubrica proposta nesta edição, sem estudo de eficácia pedagógica com participantes ou nota institucional.
