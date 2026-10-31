# IC · Dicionário de Tupi Antigo, OCR e revisão de dados

> Pesquisa e ferramentas Python para digitalizar, estruturar e revisar dados lexicográficos de Tupi Antigo, preservando fontes, Unicode, incertezas e decisões de revisão.

![Visão geral de IC · Dicionário de Tupi Antigo, OCR e revisão de dados](assets/capa.svg)

[![Verificação](https://github.com/luigiscofano/ic-pln-tupi-antigo/actions/workflows/verificacao.yml/badge.svg?branch=main)](https://github.com/luigiscofano/ic-pln-tupi-antigo/actions/workflows/verificacao.yml)

[O que faz](#o-que-este-projeto-faz) · [Módulos](#funcionalidades-e-módulos) · [Executar](#como-executar) · [Aprendizagem](#o-que-desenvolvi-e-aprendi) · [Estado atual](#estado-atual) · [Documentação](#documentação-e-navegação)

## O que este projeto faz

Documenta a iniciação científica de **Luigi Scofano de Araujo**, orientada pelo **Prof. Dr. Marcelo Finger, do IME-USP**, e reúne ferramentas para organizar dados de um dicionário de Tupi Antigo. A pesquisa trata da passagem de fontes lexicográficas para registros estruturados, preservando formas originais, grafias, traduções, localização e pendências de revisão.

O repositório contém um pipeline executável de auditoria, métricas, um notebook de demonstração, um Colab recuperado e documentação de metodologia. A demonstração usa três registros fictícios. Ele **não distribui um corpus integral validado nem oferece um tradutor automático de frases**.

## Qual problema resolve

OCR transforma a imagem de uma página em texto, mas pode perder palavras, acentos e símbolos. Uma correção automática também pode introduzir informação indevida. O desafio é estruturar o material sem apagar evidências da fonte e sem tratar uma sugestão de software como decisão linguística aprovada.

Uma palavra de entrada é mantida em `lemma_raw`; uma cópia Unicode canônica fica em `lemma_nfc`; o status continua `pending_review`. Traduções ausentes permanecem ausentes, e registros de mesma escrita não são apagados automaticamente, porque podem representar sentidos distintos.

## Funcionalidades e módulos

| Parte | O que faz | Relação com as outras |
| --- | --- | --- |
| Pipeline TSV | Importa, conserva originais, normaliza NFC, audita e exporta | Caminho principal de demonstração |
| Métricas | Calcula distância de edição, CER e WER em pares alinhados | Biblioteca separada para avaliação de texto |
| OCR opcional | Chama Tesseract local para uma imagem | Precisa de instalação e modelos de idioma externos |
| Heurísticas recuperadas | Propõe transformações de grafia do Colab | Uso explícito; não modifica o importador padrão |
| Colab histórico | Lê planilha, transforma e exporta XLSX/CSV | Requer sua interface de upload/download para execução integral |
| Documentação científica | Procedência, metodologia e protocolo de revisão | Contextualiza evidências, não executa o corpus completo |

### 1. Importação e auditoria

A entrada é TSV, um arquivo de colunas separadas por tabulação, com `id, source_id, page, line, lemma_raw, pt_raw, en_raw`. IDs devem ser únicos; página e linha são positivas. A saída conserva os registros e acrescenta uma cópia NFC. A auditoria sinaliza incompletude, caracteres problemáticos e possíveis duplicatas, sem inventar tradução ou excluir homógrafos.

NFC compõe representações Unicode equivalentes, como a+til e ã. **Não é correção ortográfica**, remoção de acentos ou escolha de uma convenção linguística.

### 2. CER, WER e OCR

CER compara caracteres; WER compara tokens separados por espaços. Ambos precisam de uma referência alinhada, e referência vazia é rejeitada. As métricas não avaliam tradução ou adequação semântica. O adaptador Tesseract é opcional e independente da demonstração TSV; a biblioteca Python não instala o binário nem os modelos de idioma.

### 3. Colab e transformações recuperadas

O [Colab](acervo/README.md) possui seis células de código para upload, imports, transformação, exportação, inspeção e download. Recebe uma planilha com forma original, português, explicação e inglês. As saídas preservam a forma original e acrescentam a proposta de transformação. O módulo `tupi/legado.py` expõe as regras para uso explícito; os testes caracterizam o programa, sem declarar acurácia linguística.

### 4. Evidências da pesquisa

[METODOLOGIA.md](docs/METODOLOGIA.md) distingue relato documental e avaliação experimental. O diário consultado tem 22 registros, classificados em 13 erros e nove notas/observações; isso não é uma taxa de falha de OCR. A tabela de 1.885 registros em 66 páginas é uma contagem declarada no relatório consultado, não uma recontagem do corpus nesta edição.

## Como executar

```sh
git clone https://github.com/luigiscofano/ic-pln-tupi-antigo.git
cd ic-pln-tupi-antigo
```

Crie um ambiente com **Python 3.12**:

```sh
python -m venv .venv
```

Ative-o no terminal que você usa:

| Sistema | Comando |
| --- | --- |
| Windows / PowerShell | `.\.venv\Scripts\Activate.ps1` |
| Linux / macOS | `source .venv/bin/activate` |

Se seu sistema oferece apenas `python3`, use esse nome ao criar o ambiente. A partir daqui, execute os comandos na raiz do repositório, com o ambiente ativado.

```sh
python -m pip install -r requirements.txt
```

Registre o kernel usado pelo executor dos notebooks:

```sh
python -m ipykernel install --user --name python3 --display-name "Python 3"
```


### Executar a demonstração e os testes

```sh
python -m unittest discover -s tests -v
python scripts/processar.py data/demo.tsv --saida build
python scripts/verificar_colab_recuperado.py
python scripts/executar_notebooks.py
```

O processamento deve informar **três registros** e `linguistic_validation: false`. Ele cria `build/registros.csv`, `build/registros.jsonl` e `build/auditoria.json`. CSV é a tabela para inspeção; JSONL guarda um registro estruturado por linha; o JSON de auditoria reúne os alertas.

O teste do Colab usa uma planilha sintética temporária e compara XLSX/CSV. O executor do notebook inicia kernel novo e exporta `.ipynb` e HTML em `build/`. Nenhum desses comandos pede conta Google, monta Drive ou usa o corpus integral.

### Usar as transformações explicitamente

```sh
python -c "from tupi.legado import normalize_navarro; print(normalize_navarro('AI'))"
```

A saída caracterizada é `AÎ`. Trate-a como proposta do algoritmo e mantenha a entrada original. O importador padrão não aplica essa transformação.

### OCR opcional e Colab completo

Para OCR, instale separadamente Tesseract e o idioma necessário. Depois, com um arquivo de imagem real chamado `pagina.png`:

```sh
python -c "from tupi.ocr import extrair; print(extrair('pagina.png', idioma='por', psm=6))"
```

Para a interface interativa do Colab, abra [o notebook recuperado](acervo/tupi_carvalho_navarro_colab.ipynb) no Google Colab e siga [a ordem das colunas e células](acervo/README.md). Upload/download não fazem parte da execução local automática.

## O que desenvolvi e aprendi

A pesquisa reúne digitalização, extração e estruturação lexicográfica, tratamento de Unicode e revisão rastreável. A edição de portfólio acrescenta ferramentas de auditoria, testes, fixtures e guias de reprodução, identificados na [procedência](docs/PROCEDENCIA.md).

**Objetivos pedagógicos:** separar fonte e interpretação; preservar diacríticos e homógrafos; tratar ausência sem inventar; distinguir execução funcional de validação linguística; avaliar OCR com referência explícita. [Atividades e rubrica](docs/OBJETIVOS_PEDAGOGICOS.md).

## Estado atual

| Disponível | Limite / evolução |
| --- | --- |
| Pipeline, auditoria e exportação | Demonstração sintética, sem corpus completo distribuído |
| Doze testes, notebook e teste XLSX/CSV | Evidência funcional dos casos exercitados |
| Colab e regras recuperadas | Sem validação linguística independente de todas as transformações |
| Adaptador OCR e protocolo de revisão de LLM | Sem benchmark real do dicionário, fine-tuning ou integração automática de LLM |

## Validação e limites

A CI executa testes em Linux/macOS/Windows e o notebook em kernel novo. O teste do núcleo recuperado não simula upload/download ou afirma execução integral no corpus. Um teste sintético de OCR também não demonstra desempenho em Tupi Antigo. [Evidências e escopo](docs/VALIDACAO.md).

## Documentação e navegação

[Biblioteca](tupi/README.md) · [Demonstração](notebooks/README.md) · [Dados](data/README.md) · [Colab](acervo/README.md) · [Scripts](scripts/README.md) · [Testes](tests/README.md) · [Guias por assunto](docs/topicos/README.md) · [Documentação](docs/README.md) · [Metodologia](docs/METODOLOGIA.md) · [Revisão](docs/PROMPTS_E_REVISAO.md) · [Branches](docs/BRANCHES.md) · [PRs](docs/PUBLICACAO.md)

### Orientação e parceria acadêmica

A orientação desta IC é de **Marcelo Finger**. A parceria acadêmica com **Calebe Rezende** é reconhecida junto ao seu projeto relacionado [Dicionário Tupi-Português](https://caleberezende.github.io/tradutorestupi/), mantido em [CalebeRezende/tradutorestupi](https://github.com/CalebeRezende/tradutorestupi). O site e o código desse dicionário são de Calebe; sua base não é atribuída automaticamente ao pipeline desta IC. [Papéis, referências e créditos](docs/PARCERIAS.md).


## Autoria, referências e licença

**Luigi Scofano de Araujo · Engenharia de Computação, Poli-USP · USP 13680334.** Fontes recuperados, componentes de terceiros e trabalhos em grupo mantêm os créditos indicados nos arquivos e na documentação.

[Direitos e créditos](DIREITOS_E_CREDITOS.md) · [Procedência](docs/PROCEDENCIA.md) · [Como contribuir](CONTRIBUTING.md) · [Mudanças](CHANGELOG.md)

## Tópicos do repositório

`python` · `natural-language-processing` · `ocr` · `unicode` · `lexicography` · `digital-humanities` · `tupi-antigo` · `data-quality` · `jupyter-notebook` · `undergraduate-research` · `usp`
