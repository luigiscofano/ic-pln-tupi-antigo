# Biblioteca de auditoria

[Início](../README.md) · [Como executar](../README.md#como-executar) · [Aprendizagem](../README.md#o-que-desenvolvi-e-aprendi) · [Estado atual](../README.md#estado-atual)

> **Nesta área:** preservação Unicode, auditoria, métricas, OCR opcional e heurísticas explícitas; o importador padrão mantém a forma original.

[Início](../README.md) · [Como executar](../README.md#como-executar) · [Aprendizagem](../README.md#o-que-desenvolvi-e-aprendi) · [Estado atual](../README.md#estado-atual)

> **Nesta área:** preservação Unicode, auditoria, métricas, OCR opcional e heurísticas explícitas; o importador padrão mantém a forma original.

- pipeline.py: importação TSV, cópia NFC, alertas e exportação.
- metricas.py: distância de edição, CER e WER em pares alinhados.
- ocr.py: adaptador opcional Tesseract local, sem benchmark real executado.

`legado.py` preserva as heurísticas recuperadas e autorizadas. O uso é explícito: o pipeline padrão conserva a forma original e aplica apenas NFC. Consulte [as regras e os testes](../docs/topicos/HEURISTICAS.md).

[Contratos](../docs/ARQUITETURA.md) · [Procedência](../docs/PROCEDENCIA.md) · [Reprodução](../docs/INSTALACAO.md).

---

**Projeto:** [IC · Dicionário de Tupi Antigo, OCR e revisão de dados](../README.md). Consulte a raiz para os requisitos e o primeiro comando; este guia aprofunda a área `tupi/`.

---

**Projeto:** [IC · Dicionário de Tupi Antigo, OCR e revisão de dados](../README.md). Consulte a raiz para os requisitos e o primeiro comando; este guia aprofunda a área `tupi/`.
