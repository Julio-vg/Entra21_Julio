
# Exercicio 9
# Faça um programa que peça o nome do cliente, a quantidade do produto (inteiro) e o preço (float).
# 
# Mostre o nome do cliente e o valor total da venda.

nome = input("Informe o Nome do Cliente: ")
quant_prod = int(input("Informe a quantidade de produto: "))
preco = float(input("Informe o preço do produto: "))
valor = preco * quant_prod
print("Cliente:", nome, "\nPaga o total de:", valor,"Reais")
