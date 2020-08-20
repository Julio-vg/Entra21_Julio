# Exercicio 9
# Faça um programa que peça 3 números inteiros e mostre o os tês em ordem crescente.
# 
# 
num1 = int(input("Digite o primeiro número:"))
num2 = int(input("Digite o segundo número:"))
num3 = int(input("Digite o terceiro número:"))

if num3 < num2:
    menor = num3
    num3 = num2
    num2 = menor
if num2 < num1:
    menor = num2
    num2 = num1
    num1 = menor
if num3 < num2:
    menor = num3
    num3 = num2
    num2 = menor
print(num1, num2, num3)