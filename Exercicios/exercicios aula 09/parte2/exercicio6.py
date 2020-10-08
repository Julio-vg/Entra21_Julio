"""Exercicio 06

Faça um programa que peça ao usuário que digite o nome de 10 pessoas. Depois mostre cada nome em linhas separadas.
"""
nomesPessoas = []

for i in range(10):
    nome = input(f"Digite o nome da pessoa {i+1}:")
    nomesPessoas.append(nome)

for i in nomesPessoas:
    print(i)