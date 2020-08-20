# Exercicio 10
# Faça um programa que peça 3 números inteiros e mostre o os tês em ordem decrescente.
# 
num1 = int(input("Digite o primeiro número:"))
num2 = int(input("Digite o segundo número:"))
num3 = int(input("Digite o terceiro número:"))

if num3 > num2:
    maior = num3
    num3 = num2
    num2 = maior
if num2 > num1:
    maior = num2
    num2 = num1
    num1 = maior
if num3 > num2:
    maior = num3
    num3 = num2
    num2 = maior
print(num1, num2, num3)