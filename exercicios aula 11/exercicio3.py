"""Exercício 3

(use somente o while)

Faça um programa que peça o nome e a idade do cliente e mostre a seguinte mensagem:

Para mairores de 18 anos: Entrada Permitida
Para menores de 18 anos: Entrada proibida.

Depois mostre a lista dos nomes (somente os nomes) das pessoas com entrada permitida.

Regras:
- O programa não pode aceitar nomes em branco. Caso não se digite um nome o programa deve mostrar a mensagem "Nome em branco" e repetir o código.
- Caso o usuário deixe em branco a idade, o progama deve mostrar uma mensagem: "Obrigado pela preferência" e terminar logo em seguida.
"""
idadelista = []
nomelista = []
while True:
    nome = input("Informe o seu nome:")
    if nome == '':
        print("Nome Em Branco")
        continue
    nomelista.append(nome)
    idade = input("Informe a sua idade:")
    if idade == '':
        print("Obrigado pela preferência")
        break
    idadelista.append(idade)
    if idade >= '18':
        print("Entrada Permitida")
    elif idade < '18':
        print("Entrada Proibida")
    escolha = input("Desejar Cadastrar outro nome S/N:")
    if escolha == 'N' or escolha == 'n':
        break
    for i in range(len(nomelista)):
        if idadelista[i] >= '18':
            print(f"Clientes Com Entrada Permitida:{nomelista[i]}")
