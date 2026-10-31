# Dados e rastreabilidade

data/demo.tsv contém três registros sintéticos. EXEMPLO-Ã e TESTE-g̃ são fixtures, não verbetes lexicográficos validados. Duas linhas com mesmo lema ilustram homografia/duplicação aparente; uma tradução em inglês vazia ilustra ausência.

| Campo | Contrato |
| --- | --- |
| id | Identificador único não vazio |
| source_id | Identificador editorial local obrigatório |
| page / line | Inteiros positivos |
| lemma_raw / pt_raw / en_raw | Texto original preservado, podendo conter ausência |
| lemma_nfc | Forma Unicode NFC derivada |
| status | pending_review nesta implementação |

JSONL preserva texto e estrutura; CSV usa UTF-8 com BOM, cabeçalho e quoting. Não abra dados não revisados como fórmulas de planilha: o exportador conserva o texto, sem modificar campos arbitrariamente. Nenhum exemplo inclui dado pessoal ou credencial.

Para um corpus real, mantenha catálogo editorial, permissão de distribuição, páginas de origem, decisões de revisão e divisão entre raw/derivado/revisado. Os PDFs e tabelas integrais encontrados foram usados como contexto privado, sem atribuir licença nova às obras.
