"""Exercicio 05

Faça um programa que peça ao usuário digitar a quantidade de vendas do dia. Cadastre cada venda separadaemnte e depois mostre a média e o valor total vendido no dia.
"""
vendas = int(input("Informe a quantidade de vendas hoje:"))
vendasTotal = []
for i in range(vendas):
    valor = float(input(f"Informe o valor da venda {i+1}:"))
    vendasTotal.append(valor)

media = sum(vendasTotal) / len(vendasTotal)
total = sum(vendasTotal)
print(f"""Média de vendas do dia:{media} 
Total de Vendas do dia:{total} """)
