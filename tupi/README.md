# Biblioteca de auditoria

- pipeline.py: importação TSV, cópia NFC, alertas e exportação.
- metricas.py: distância de edição, CER e WER em pares alinhados.
- ocr.py: adaptador opcional Tesseract local, sem benchmark real executado.

`legado.py` preserva as heurísticas recuperadas e autorizadas. O uso é explícito: o pipeline padrão conserva a forma original e aplica apenas NFC. Consulte [as regras e os testes](../docs/topicos/HEURISTICAS.md).

[Contratos](../docs/ARQUITETURA.md) · [Procedência](../docs/PROCEDENCIA.md) · [Reprodução](../docs/INSTALACAO.md).
