<p align="center"><img src="assets/capa.svg" alt="IC · PLN aplicado ao Tupi Antigo" width="100%"></p>

# IC · PLN aplicado ao Tupi Antigo

**Preservar a fonte, explicitar a incerteza e tornar a revisão auditável.**

[![Verificação](https://github.com/luigiscofano/ic-pln-tupi-antigo/actions/workflows/verificacao.yml/badge.svg?branch=main)](https://github.com/luigiscofano/ic-pln-tupi-antigo/actions/workflows/verificacao.yml)

Portfólio de **Luigi Scofano de Araujo · Engenharia de Computação, Poli-USP · USP 13680334**. Organização e complementos de 2026, distinguindo acervo recuperado e implementações novas. [Procedência](docs/PROCEDENCIA.md).

## Orientação, parcerias e trabalhos relacionados

A IC de **Luigi Scofano de Araujo** tem orientação do **Prof. Dr. Marcelo Finger (IME-USP)**. A parceria acadêmica com **Calebe Rezende** é reconhecida junto ao seu projeto relacionado, o **Dicionário Tupi-Português**, mantido em [CalebeRezende/tradutorestupi](https://github.com/CalebeRezende/tradutorestupi).

**[Consultar o dicionário do Calebe →](https://caleberezende.github.io/tradutorestupi/)** · **[Parcerias, papéis e créditos →](docs/PARCERIAS.md)**

A contribuição desta IC está na digitalização, estruturação e revisão de dados lexicográficos. O site e o código do dicionário referenciado têm seus créditos atribuídos a Calebe Rezende.

## Objetivos pedagógicos em destaque

- **Separar fonte e interpretação** — Manter lemma_raw e cópia NFC.
- **Tratar ausência sem inventar** — Manter tradução vazia.
- **Preservar homógrafos** — Manter IDs distintos para lema igual.
- **Avaliar OCR** — Calcular CER/WER em pares alinhados.
- **Distinguir validações** — Separar aprovação funcional e correção linguística.
- **Documentar revisão** — Manter pendências até uma decisão documentada.

**[Atividades, evidências e rubrica →](docs/OBJETIVOS_PEDAGOGICOS.md)**

## Execute e experimente

```sh
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
python scripts/processar.py data/demo.tsv --saida build
python scripts/verificar_colab_recuperado.py
python scripts/executar_notebooks.py
```

Ambiente: **Python 3.12, Unicode e Jupyter**. [Instalação detalhada](docs/INSTALACAO.md).

## Encontre cada parte

**[Guias por assunto](docs/topicos/README.md) · [Mapa de branches](docs/BRANCHES.md) · [PRs e entregas](docs/PUBLICACAO.md)**

| Diretório | Conteúdo |
| --- | --- |
| [tupi/](tupi/README.md) | Auditoria, métricas, OCR opcional e documentação de revisão. |
| [acervo/](acervo/README.md) | Colab recuperado, sanitizado e autorizado, com guia de reprodução. |
| [notebooks/](notebooks/README.md) | Demonstração nova executável com fixtures sintéticas. |
| [data/](data/README.md) | Três linhas fictícias; não é o corpus histórico nem léxico validado. |
| [tests/](tests/README.md) | Preservação Unicode, homógrafos, exportação e métricas. |
| [scripts/](scripts/README.md) | CLI de importação, relatórios e execução do notebook. |
| [assets/](assets/README.md) | Fluxo metodológico e gráfico descritivo do diário. |
| [docs/](docs/README.md) | Arquitetura, objetivos, reprodução, apresentação e evidência |

## Verificação e limites

Doze testes unittest cobrem preservação, alertas, homógrafos, round-trip CSV/JSONL, entradas inválidas, NFC, distâncias, referências vazias e caracterização das heurísticas recuperadas. O núcleo do Colab também transforma uma planilha sintética, com comparação das saídas XLSX/CSV. O notebook novo contém três células de código com asserções.

Sem benchmark real de OCR, validação linguística protocolada, fine-tuning ou tradutor; sem corpus integral distribuído; Colab sanitizado e funções derivadas disponíveis no acervo; adaptador OCR não avaliado em corpus real.

**[Validação →](docs/VALIDACAO.md)** · **[Arquitetura e decisões →](docs/ARQUITETURA.md)**

Use o [roteiro de apresentação](docs/APRESENTACAO.md) e confira os [PRs reais](docs/PUBLICACAO.md). As branches representam organização atual, sem datas retroativas ou revisões fictícias.

[Contribuir](CONTRIBUTING.md) · [Direitos e créditos](DIREITOS_E_CREDITOS.md) · [Referências](docs/REFERENCIAS.md) · [Mudanças](CHANGELOG.md)

**CI confirmada:** [testes aprovados](https://github.com/luigiscofano/ic-pln-tupi-antigo/actions/runs/41232865418). Consulte o registro de [validação remota](docs/validacao-remota.json).
