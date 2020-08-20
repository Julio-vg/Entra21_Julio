# Exercicio 6
# Escreva um programa que peça 2 números e mostre eles em ordem crescente

num1 = int(input("Digite o primeiro número:"))
num2 = int(input("Digite o segundo número:"))

if num1 > num2:
    print(num2,num1)
else:
    print(num1,num2)