"""Métricas para pares alinhados; nenhum benchmark de OCR é presumido."""
def distancia(a,b):
    anterior=list(range(len(b)+1))
    for i,x in enumerate(a,1):
        atual=[i]
        for j,y in enumerate(b,1):atual.append(min(atual[-1]+1,anterior[j]+1,anterior[j-1]+(x!=y)))
        anterior=atual
    return anterior[-1]
def cer(referencia,hipotese):
    if not referencia:raise ValueError('CER indefinido para referência vazia')
    return distancia(referencia,hipotese)/len(referencia)
def wer(referencia,hipotese):
    r,h=referencia.split(),hipotese.split()
    if not r:raise ValueError('WER indefinido para referência sem palavras')
    return distancia(r,h)/len(r)
