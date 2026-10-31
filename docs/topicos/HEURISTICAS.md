# Regras recuperadas e uso explícito

`tupi/legado.py` preserva as funções do Colab autorizado. As substituições e exceções são determinísticas, mas não demonstram equivalência linguística para toda entrada. Use `normalize_navarro` somente como proposta derivada, mantendo a forma original ao lado.

```python
from tupi.legado import normalize_navarro
original = "AI"
proposta = normalize_navarro(original)
assert original == "AI" and proposta == "AÎ"
```

O exemplo caracteriza o código recuperado; não é uma validação de dicionário. O importador padrão aplica NFC e deixa o estado `pending_review`, sem chamar as heurísticas.

## Verificar

```sh
python -m unittest discover -s tests -v
python scripts/verificar_colab_recuperado.py
```

O segundo comando executa as células de regras e exportação do acervo em diretório temporário. Verifica formato XLSX/CSV, manutenção da coluna original e organização das colunas. A interface de upload/download e o corpus real não são testados por esse comando.
