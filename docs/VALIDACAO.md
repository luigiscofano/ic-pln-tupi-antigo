# Validação

## Evidência local — 31/10/2026

Nove testes unittest de preservação, alertas, homógrafos, round-trip CSV/JSONL, entradas inválidas, NFC com diacríticos, distâncias conhecidas e referências vazias. Notebook novo com três células de código e asserções.

## Limites da conclusão

Sem benchmark real de OCR, validação linguística protocolada, fine-tuning ou tradutor; sem corpus integral distribuído; Colab e funções derivadas aguardam autorização específica; adaptador OCR não avaliado em corpus real.

Um workflow configurado ou PR aberto não demonstra aprovação. A evidência remota e o commit testado serão registrados após conclusão do GitHub Actions.

O [registro local estruturado](validacao-local.json) preserva o comando e o log efetivamente obtidos.

As três células do notebook novo passaram localmente via IPython em processo novo. Esse modo não valida o protocolo do kernel Jupyter; a CI executa a verificação via nbclient. O acervo Colab não integra a versão pública enquanto aguarda autorização.
