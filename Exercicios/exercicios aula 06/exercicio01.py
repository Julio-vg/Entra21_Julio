#Execicios 01
#Escreva um programa que calcule a porcentagem de comissão de vendedores com as seguintes condições
#Venda Total
#de R$ 0.00 a R$ 30000.00 - 0%
#de R$ 30000.01 a R$ 50000.00 - 1.5%
#de R$ 50000.01 a R$ 100000.00 - 2.5%
#Acima de R$ 100000.00 - 3.5%

venda_total = float(input("Informe o valor total de vendas:"))

if venda_total >= 0.00 and venda_total <= 30000.00:
    print("Valor de comissão não atingido!")

elif venda_total >= 30000.01 and venda_total <= 50000.00:
    print("Total de comissão recebido:", venda_total*(1.5/100))

elif venda_total >= 50000.01 and venda_total <= 100000.00:
    print("Total de comissão recebido:", venda_total*(2.5/100))

elif venda_total > 100000.00:
    print("Total de comissão recebido:", venda_total*(3.5/100))