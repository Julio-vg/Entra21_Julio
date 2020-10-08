"""Exercício 02

O id de um cliente é um código único (só aquela pessoa tem) composto por números inteiros que inicia do número 1 e vai aumentando de 1 em 1 enquanto for necessário.

Exemplo:
id: 1
Nome: Dudu

id: 2
Nome: Marta

id: 3
Nome: Pedro


ATENÇÃO!!!!
O id é um número atribuido automáticamente! O cliente não escolhe o número. O seu programa deve fazer o cadastro deste id automaticamente.


Com isso, crie um cadastro de clientes que receba o id, nome e idade. Depois mostre os dados dos clientes individualmente.
(cadastre no minimo 4 clientes)
"""
nome_lista = []
idade_lista = []
ids = []

for i in range(5):
    nome = input(f"Digite o nome do cliente {i+1} :")
    idade = int(input(f"Digite a idade do cliente {i+1} :"))
    nome_lista.append(nome)
    idade_lista.append(idade)
    ids.append(i+1)

cadastros = len(nome_lista)

for i in range(cadastros):
    print(f"""
Nome Cadastrado: {nome_lista[i]}

Idade Cadastrada: {idade_lista[i]}

ID do cliente: {ids[i]} 

""")