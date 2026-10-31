# Protocolo proposto para os módulos novos

Este documento descreve o software novo e um protocolo de avaliação futura. Não relata estatísticas de corpus ou resultados de materiais privados.

1. Fornecer TSV com o esquema documentado em DADOS.md.
2. Manter campos raw sem substituí-los pela cópia NFC.
3. Gerar alertas de qualidade estrutural, preservando homógrafos.
4. Revisar cada alerta com referência autorizada e registrar a decisão.
5. Exportar CSV/JSONL preservando identificadores editoriais locais.
6. Para avaliar OCR, preparar referência humana e hipóteses alinhadas; declarar Unicode, tokenização e denominadores antes de calcular CER/WER.

Os testes atuais demonstram contratos do software em fixtures sintéticas. Não medem taxa de erro em um dicionário real ou qualidade de tradução.
