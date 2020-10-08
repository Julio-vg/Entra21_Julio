# Exercicio 7
# Faça um programa que peça 3 números inteiros e mostre o menor número.

num1 = int(input("Digite o primeiro número:"))
num2 = int(input("Digite o segundo número:"))
num3 = int(input("Digite o terceiro número:"))

menor = num1
if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3
print("Menor número:", menor)




