# Colab recuperado · março de 2026

[Início](../README.md) · [Como executar](../README.md#como-executar) · [Aprendizagem](../README.md#o-que-desenvolvi-e-aprendi) · [Estado atual](../README.md#estado-atual)

> **Nesta área:** material recuperado, com sua origem e limitações; não confunda preservação histórica com aprovação pela suíte atual.

[Início](../README.md) · [Como executar](../README.md#como-executar) · [Aprendizagem](../README.md#o-que-desenvolvi-e-aprendi) · [Estado atual](../README.md#estado-atual)

> **Nesta área:** material recuperado, com sua origem e limitações; não confunda preservação histórica com aprovação pela suíte atual.

[Abra o notebook recuperado](tupi_carvalho_navarro_colab.ipynb). A publicação foi autorizada pelo autor. A cópia preserva o código e remove saídas antigas e metadados de sessão.

| Célula de código | Função | Dependência |
| --- | --- | --- |
| 1 | Upload e escolha da planilha | Interface Google Colab |
| 2 | Imports | Python e openpyxl |
| 3 | Regras e exceções ortográficas | re e unicodedata |
| 4 | Nova tabela e exportação XLSX/CSV | Workbook de entrada |
| 5 | Inspeção de linhas selecionadas | Tabela gerada |
| 6 | Download dos arquivos | Interface Google Colab |

## Executar no Colab

1. Abra o arquivo no Google Colab e instale `openpyxl==3.1.5`, se necessário.
2. Envie uma cópia de trabalho de uma planilha autorizada. A primeira aba deve ter, nesta ordem: forma original, português, explicação em português e inglês.
3. Execute as células na ordem. A saída tem TUPI O.O., TUPI O.N., PTBR, ENUS e EXPLICAÇÃO PTBR.
4. Compare sempre a forma proposta com a forma original e com a fonte; o algoritmo não decide validade linguística.

Os botões de upload/download dependem do Colab. A CI testa o núcleo de transformação separadamente, com planilha sintética, sem simular essa interface ou usar o corpus real. A célula de inspeção contém números de linhas do acervo; em uma planilha menor, essas posições podem estar vazias.

O relatório de pesquisa distingue transformação reprodutível de validação linguística. Este notebook não demonstra, por si só, a acurácia das regras ou a execução completa sobre o corpus.

[Ferramentas novas](../tupi/README.md) · [Procedência](../docs/PROCEDENCIA.md) · [Instalação](../docs/INSTALACAO.md)

---

**Projeto:** [IC · Dicionário de Tupi Antigo, OCR e revisão de dados](../README.md). Consulte a raiz para os requisitos e o primeiro comando; este guia aprofunda a área `acervo/`.

---

**Projeto:** [IC · Dicionário de Tupi Antigo, OCR e revisão de dados](../README.md). Consulte a raiz para os requisitos e o primeiro comando; este guia aprofunda a área `acervo/`.
