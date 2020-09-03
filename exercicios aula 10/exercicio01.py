"""
Exercício 01

Crie um programa que cadastre 5 clientes. 

Cada cliente possui: Nome, sexo, Telefone
(Guarde estes dados em listas separadas).

Depois mostre os dados cadastrados no seguinte formato:



***********************************
Relatório de clientes cadastrados 
***********************************
Nome: 
Sexo:
Telefone:
***********************************
"""

cadastroNomes = []
cadastroSexo = []
cadastroTele = []

for i in range(5):
    nome = input("Informe seu nome:")
    sexo = input("Informe o seu sexo F/M:")
    telefone = int(input("Digite o seu telefone:"))
    cadastroNomes.append(nome)
    cadastroSexo.append(sexo)
    cadastroTele.append(telefone)

cadastro = len(cadastroNomes)

for i in range(cadastro):
    print(f"""
Nome Cadastrado: {cadastroNomes[i]}
Sexo Cadastrado: {cadastroSexo[i]}
Telefone Cadastrado: {cadastroTele[i]}
""")
