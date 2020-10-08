# Exercicio 10
# Faça um programa que peça o nome de 2 produtos, a quantidade comprada de cada produto (inteiro) e o valor (float) de cada um.
# 
# Mostre o nome a quantidade, preço por unidade e o total de cada produto.

prod1 = input("Informe o nome do produto 1:")
prod2 = input("Informe o nome do produto 2:")

quant_prod1 = int(input("Informe a quantidade do produto 1:"))
quant_prod2 = int(input("Informe a quantidade do produto 2:"))

valor_prod1 = float(input("Informe o valor do produto 1:"))
valor_total1 = valor_prod1 * quant_prod1

valor_prod2 = float(input("Informe o valor do produto 2:"))
valor_total2 = valor_prod2 * quant_prod2

print("Nome do Produto 1", prod1,",Quantidade", quant_prod1,",Preço por unidade", valor_prod1,",Total", valor_total1,"Reais")
print("Nome do produto 2", prod2,",Quantidade", quant_prod2,",Preço por unidade", valor_prod2,",Total", valor_total2,"Reais")


