"""Exercicio 09

Faça um programa que pegue uma lista de valores e separe em 2 listas. Uma com valores menores que 500.00 e outra com maiores ou igual.

Depois motre o maior e o menor valor da cada lista.

vandas = [100.00, 500.00, 258.50, 710.00, 50.50,750.00, 10.00, 1050.00, 859.75, 199.05, 500.50,750.00, 568.60, 950.00, 950.00, 89.90, 2500.00, 1750.00,500.00]
"""
vandas = [100.00, 500.00, 258.50, 710.00, 50.50,750.00, 10.00, 1050.00, 859.75, 199.05, 500.50,750.00, 568.60, 950.00, 950.00, 89.90, 2500.00, 1750.00,500.00]

lista1 = []
lista2 = []

for i in vandas:
    if i >= 500.00:
        lista2.append(i)
    else:
        lista1.append(i)

print(f"""Maior valor da lista 1: {max(lista1)} 
Menor valor da lista 1: {min(lista1)} 
Maior valor da lista 2: {max(lista2)} 
Menor valor da lista 2: {min(lista2)} 
""")

