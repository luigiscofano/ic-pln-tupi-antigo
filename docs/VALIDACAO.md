# Validação

## Ampliação autorizada — 31/10/2026

Os 12 testes unittest passaram localmente. Eles cobrem preservação, alertas, homógrafos, round-trip CSV/JSONL, entradas inválidas, NFC, distância de edição, referências vazias e caracterização das heurísticas recuperadas. O teste de regressão confirma que o importador padrão não aplica essas heurísticas.

`python scripts/verificar_colab_recuperado.py` passou: executa o núcleo do Colab original em uma planilha sintética temporária, confere o número e a ordem das colunas, preserva a forma original e compara XLSX com CSV. Não requer conta Colab nem envia dados.

## Evidência remota confirmada

[Execução 41232865418](https://github.com/luigiscofano/ic-pln-tupi-antigo/actions/runs/41232865418) aprovada no commit `8320f6dcdc4c7dc638f78251810992b731f74da8`, em `main`.

- **notebooks**: success.
- **testes (macos-15)**: success.
- **testes (windows-latest)**: success.
- **testes (ubuntu-24.04)**: success.

O job de notebooks executou o núcleo recuperado e as três células de código do notebook novo via kernel Jupyter e nbclient. O acervo histórico passou na validação de esquema e ausência de saídas; suas células interativas de upload/download não foram executadas integralmente.

### Artefatos

O notebook executado e o HTML estão nos artefatos da execução. O acesso pode exigir login no GitHub e há prazo de retenção.

- [notebook-executado-html](https://github.com/luigiscofano/ic-pln-tupi-antigo/actions/runs/41232865418/artifacts/13054780804) — retenção até 2027-01-29T19:09:26Z.
- [evidencia-ubuntu-24.04](https://github.com/luigiscofano/ic-pln-tupi-antigo/actions/runs/41232865418/artifacts/13054581348) — retenção até 2027-01-29T19:09:26Z.
- [evidencia-macos-15](https://github.com/luigiscofano/ic-pln-tupi-antigo/actions/runs/41232865418/artifacts/13054576403) — retenção até 2027-01-29T19:09:26Z.
- [evidencia-windows-latest](https://github.com/luigiscofano/ic-pln-tupi-antigo/actions/runs/41232865418/artifacts/13053819904) — retenção até 2027-01-29T19:09:26Z.

[Registro estruturado desta execução](validacao-remota.json).

## Histórico e limites

O [registro local anterior](validacao-local.json) documenta a etapa de nove testes, anterior à autorização de publicação do acervo. Seu campo de autorização é histórico; a situação atual está em [PROCEDENCIA.md](PROCEDENCIA.md).

O adaptador OCR também passou em teste local com imagem sintética de texto latino TESTE 123, idioma eng e PSM 6. Não representa avaliação de Tupi Antigo ou do corpus histórico.

Os resultados demonstram comportamento nos casos exercitados. Não constituem benchmark real de OCR, validação linguística protocolada, fine-tuning ou tradutor. O corpus integral e obras editoriais não são distribuídos. Mudanças apenas documentais posteriores não ampliam a evidência funcional do commit identificado.
