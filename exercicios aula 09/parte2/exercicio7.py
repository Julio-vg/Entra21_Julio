"""Exercicio 07

Faça um programa que receba 10 idades e mostre a seguinte mensagem:

Para maiores de 18 anos: Ingreços da Rave liberado!
De 16 a 18 anos: Ingreços de cinema liberado 
De 13 a 16 anos: Ingreços para fliperama liberado
Menores de 13 anos: Psicina de bolinhas liberado
"""
idadeCadastro = []

for i in range(10):
    idade = int(input(f"Digite a idade da pessoa {i+1}:"))
    idadeCadastro.append(idade)

for i in idadeCadastro:
    if i >= 18:
        print(f"Idade: {i} - Ingreços da Rave Liberado!")
    elif i >= 16:
        print(f"Idade: {i} - Ingreços de cinema liberado")
    elif i >= 13:
        print(f"Idade: {i} - Ingreços para fliperama liberado")
    else:
        print(f"Idade: {i} - Piscina de bolinhas liberado")

