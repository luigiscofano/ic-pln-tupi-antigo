# Validação

## Evidência local — 31/10/2026

Nove testes unittest de preservação, alertas, homógrafos, round-trip CSV/JSONL, entradas inválidas, NFC com diacríticos, distâncias conhecidas e referências vazias. Notebook novo com três células de código e asserções.

## Limites da conclusão

Sem benchmark real de OCR, validação linguística protocolada, fine-tuning ou tradutor; sem corpus integral distribuído; Colab e funções derivadas aguardam autorização específica; adaptador OCR não avaliado em corpus real.

Um workflow configurado ou PR aberto não demonstra aprovação. A evidência remota e o commit testado serão registrados após conclusão do GitHub Actions.

O [registro local estruturado](validacao-local.json) preserva o comando e o log efetivamente obtidos.

As três células do notebook novo passaram localmente via IPython em processo novo. Esse modo não valida o protocolo do kernel Jupyter; a CI executa a verificação via nbclient. O acervo Colab não integra a versão pública enquanto aguarda autorização.

## Evidência remota confirmada

[Execução 41227951683](https://github.com/luigiscofano/ic-pln-tupi-antigo/actions/runs/41227951683) aprovada no commit `6135c50ef5e4778c174d6c767237ea652fa8451d`.

- **notebooks**: success.
- **testes (windows-latest)**: success.
- **testes (ubuntu-24.04)**: success.
- **testes (macos-15)**: success.

Os artefatos podem exigir login no GitHub e têm prazo de retenção; os fontes permanecem no repositório.

- [evidencia-windows-latest](https://github.com/luigiscofano/ic-pln-tupi-antigo/actions/runs/41227951683/artifacts/13052705873) — retenção até 2027-01-29T18:08:51Z.
- [evidencia-macos-15](https://github.com/luigiscofano/ic-pln-tupi-antigo/actions/runs/41227951683/artifacts/13052476950) — retenção até 2027-01-29T18:08:51Z.
- [evidencia-ubuntu-24.04](https://github.com/luigiscofano/ic-pln-tupi-antigo/actions/runs/41227951683/artifacts/13052337414) — retenção até 2027-01-29T18:08:51Z.
- [notebook-executado-html](https://github.com/luigiscofano/ic-pln-tupi-antigo/actions/runs/41227951683/artifacts/13052162800) — retenção até 2027-01-29T18:08:51Z.

O commit acima identifica exatamente a versão testada. Atualizações documentais posteriores não ampliam a conclusão funcional.

O adaptador OCR também passou em teste local com imagem sintética de texto latino TESTE 123, idioma eng e PSM 6. Não representa avaliação de Tupi Antigo ou do corpus histórico.
