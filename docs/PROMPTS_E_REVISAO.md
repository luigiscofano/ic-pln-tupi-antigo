# Proposta de revisão dos dados novos

O software não chama modelos de linguagem. Para integrar um no futuro, o contrato deve exigir os campos do esquema, deixar ausências vazias e manter status pending_review até haver decisão documentada. Saída de modelo não deve substituir o campo raw nem ser tratada como validação linguística automática.

No fixture atual, confirme os três IDs, preserve as duas linhas de mesmo lema e mantenha vazio o campo de tradução ausente. Esse é um exercício de verificação estrutural, sem inferir conhecimento do Tupi Antigo a partir de dados fictícios.
