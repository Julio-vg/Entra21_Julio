

# 2) Crie uma lista com 10 números qualquer.
# 
# Usando as funções da lista responda:
# 
# Quantos itens tem a lista?
# Qual é o número maior?
# Qual é o número menor?
# Qual é o resultado da soma da lista?
# 
# 
# 

lista = [ 10, 20, 30, 95, 12, 5, 7, 65, 14, 33]
itens = len(lista)
maior = max(lista)
menor = min(lista)
total = sum(lista)
print(f"""Total De Itens Na Lista: {itens} 
Maior Número: {maior} 
Menor Número: {menor}
Soma Total da lista: {total}""")
