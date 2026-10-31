# Decisões de engenharia

| Decisão | Motivo | Consequência |
| --- | --- | --- |
| Separar acervo e código novo | Preservar procedência | Não corrigir silenciosamente o passado |
| Testes com entradas fixas ou sementes declaradas | Reproduzir falhas | Não usar resultado aleatório como evidência sem repetir |
| Scripts sem caminhos pessoais | Facilitar reprodução | Ferramentas precisam estar instaladas ou indicadas por ambiente |
| Contratos e erros explícitos | Evitar saídas plausíveis para entradas inválidas | Casos negativos fazem parte da suíte |
| PRs por entregas verificáveis | Facilitar revisão | Datas refletem organização atual |

Decisões específicas e diferenças em relação ao histórico estão em [ARQUITETURA.md](ARQUITETURA.md) e [PROCEDENCIA.md](PROCEDENCIA.md). Limites: Sem benchmark real de OCR, validação linguística protocolada, fine-tuning ou tradutor; sem corpus integral distribuído; obras editoriais e corpus integral não distribuídos; adaptador OCR não avaliado em corpus real.
