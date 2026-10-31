# Experimentos e critérios de aceitação

## Exercício guiado

Execute os exemplos de [INSTALACAO.md](INSTALACAO.md) e anote a previsão antes de rodar. A saída só conta como evidência depois de comparada com o contrato de [ARQUITETURA.md](ARQUITETURA.md).

## Casos de fronteira e referência

Nove testes unittest de preservação, alertas, homógrafos, round-trip CSV/JSONL, entradas inválidas, NFC com diacríticos, distâncias conhecidas e referências vazias. Notebook novo com três células de código e asserções.

Leia a suíte e escolha um caso que quebra uma solução ingênua. Explique o motivo, reduza a entrada ao menor contraexemplo e proponha uma correção sem alterar o contrato silenciosamente. Use referência independente quando disponível.

## O que não concluir

Sem benchmark real de OCR, validação linguística protocolada, fine-tuning ou tradutor; sem corpus integral distribuído; materiais privados não publicados; adaptador OCR não avaliado em corpus real.

Não use tempo isolado ou gráfico atraente como prova de correção. Registre ambiente, entrada, saída, versão e limitações relevantes.
