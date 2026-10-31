# Metodologia e hierarquia de evidências

## O que os materiais sustentam

O diário consultado registra 22 ocorrências entre abril e julho de 2025: 13 erros e nove notas/observações. É um diário documental, não um conjunto de tentativas controladas; contar suas categorias não produz uma taxa de erro de OCR ou LLM. O relatório revisado consultado descreve uma tabela central de 1.885 registros em 66 páginas. Essas contagens são declaradas no relatório, não recalculadas sobre a tabela integral nesta edição.

As fontes documentam digitalização, tentativas de OCR com Tesseract/Google Vision, prompting para estruturação e organização em planilhas. O Colab recuperado acrescenta evidência de código de transformação XLSX/CSV disponível em março de 2026. Não comprova o desempenho global do fluxo.

## Taxonomia operacional

| Falha observada nos registros | Possível impacto | Controle proposto |
| --- | --- | --- |
| Primeira/última entrada omitida | Perda silenciosa de verbetes | Conferir bordas e contar entradas por página |
| Diacrítico alterado | Mudança da forma linguística | Preservar imagem/raw e comparar grafemas |
| Classe ou tema confundido com lema | Coluna incorreta | Colunas explícitas e revisão humana |
| Hífen e quebra de linha | Divisão de uma entrada | Não recompor automaticamente sem evidência |
| Tradução inventada para lacuna | Falso dado lexicográfico | Campo vazio e pending_review |
| Coluna deslocada | Tradução ligada ao lema errado | Conferência por página e identificador |

## Experimento futuro de OCR

1. Definir páginas e critérios de inclusão antes da medição.
2. Transcrever referência humana, com adjudicação de divergências.
3. Fixar mecanismo, versão, idioma, PSM e pré-processamento.
4. Alinhar referência/hipótese, declarar Unicode e tokenização.
5. Calcular CER/WER por página e agregação com denominadores explícitos.
6. Separar teste de OCR de avaliação das sugestões de LLM.
7. Publicar limites, exemplos de falhas e dados com direitos de distribuição verificados.

Nada nesta proposta equivale a um benchmark já concluído. A suíte atual valida funcionamento do software em fixtures, não correção linguística do corpus.
