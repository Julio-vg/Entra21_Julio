"""Exercício 03

3.1) Crie um programa que cadastre o id, nome, sexo e a idade de 5 clientes.

3.2) Depois mostre os dados dos 5 clientes.

3.3) Peça para que o usuário escolha um id de um cliente e mostre as informações deste cliente.

3.4) Crie um filtro que ao digitar um id de um cliente mostre as seguintes informações:
- Para menores de 17 anos: Entrada Proibida
- Para maiores de 17 anos: Entrada Liberada
- Para o sexo Feminino: 50% de desconto
- Para o sexo Masculino: 5% de desconto
"""
id_lista = []
nome_lista = []
sexo_lista = []
idade_lista = []

for i in range(3):
    nome = input(f"Informe o nome do cliente {i+1}:")
    sexo = input(str(f"Informe o sexo do cliente {i+1} F/M:"))
    idade = int(input(f"Informe a idade do cliente {i+1}:"))
    nome_lista.append(nome)
    sexo_lista.append(sexo)
    idade_lista.append(idade)
    id_lista.append(i+1)

cadastro = len(nome_lista)

for i in range(cadastro):
    print(f"""
Nome:{nome_lista[i]}
Sexo:{sexo_lista[i]}
Idade:{idade_lista[i]}
ID:{id_lista[i]}
""")

ident = int(input("Digite uma ID:"))

for i in range(3):
    if id_lista[i] == ident:
        print(f"""
Nome:{nome_lista[i]}
Sexo:{sexo_lista[i]}
Idade:{idade_lista[i]}
""")
        
        if sexo_lista[i] == 'M' or sexo_lista[i] == 'm':
            print("5% de Desconto.")
        elif sexo_lista[i] == 'F' or sexo_lista[i] == 'f':
            print("50% de Desconto")
        if idade_lista[i] >= 17:
            print("Entrada Liberada")
        elif idade_lista[i] < 17:
            print("Entrada Proibida")
            


            
