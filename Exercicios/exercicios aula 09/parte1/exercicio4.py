"""Exercicio 04

Faça um programa de cadastro de pessoas que receba 10 nomes, idades e e-mails e salve cada um em uma lista.

Depois mostre as listas separadamente 
(print (lista) já é o suficiente)
"""
cadastroNome = []
cadastroIdade = []
cadastroEmail = []

for i in range(10):
    nome = input("Informe o seu nome:")
    cadastroNome.append(nome)
    idade = input("Informe a sua idade:")
    cadastroIdade.append(idade)
    email = input("Informe o seu e-mail:")
    cadastroEmail.append(email)

print(f"""Nomes Cadastrados: {cadastroNome}  

Idades Cadastradas: {cadastroIdade} 

E-mails Cadastrados: {cadastroEmail} """)
    