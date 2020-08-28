"""Exercicio 03

Faça um programa que peça 10 notas do aluno. Faça a média e mostre as seguintes mensagens:

Para 7 a 10 - Aprovado
Para 5.5 a 7 - Recuperação 
Para menor de 5.5 - Reprovado
"""
pontos = []
for i in range(10):
    nota = float(input(f"Digite a nota {i+1}: "))
    pontos.append(nota)

media = sum(pontos) / len(pontos)

if media >= 7:
    print("Aluno Aprovado")
elif media >= 5.5:
    print("Aluno em Recuperação")
else:
    print("Aluno Reprovado")