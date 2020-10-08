"""Exercício 4

(use o conhecimento que foi passado no curso)

Crie um programa com um menu interativo:

-----
Cadastro de pessoas v1.0

A) Cadastrar Pessoa
B) Ver todos os nomes cadastrados:
C) Ver cadastro pelo nome:
D) Apagar um cadastro pelo nome:
S) Sair

-----



Para A: Cadastre os dados do cliente (Nome, idade, sexo, telefone
Para B: Mostre todos os nomes dos clientes (só os nomes)
Para C: Digite o nome do cliente e mostre todos os dados dele.
Para D: Digite o nome do cliente e o apague do cadastro
Para S: Mostre uma mensagem de despedida e termine o programa
Para qualquer outro valor: Mostre "Opção invalida"
"""
listaNome = []
listaIdade = []
listaSexo = []
listaTele = []
opcao = ''

while opcao != 'S' or opcao != 's':
    print('\n')
    opcao = input("""Bem Vindo ao menu de cadastro de clientes:
A) Cadastrar Dados 
B) Clientes Cadastrados
C) Consultar Cadastro
D) Excluir Cadastro
S) Sair

Escolha a opção desejada: """)
    
    print('\n')
    if opcao == 'A' or opcao == 'a':
        nome = input("Informe o seu nome:")
        listaNome.append(nome)
        idade = int(input("Informe a sua idade:"))
        listaIdade.append(idade)
        sexo = input("Informe o seu sexo F/M:")
        listaSexo.append(sexo)
        telefone = int(input("Informe o seu telefone:"))
        listaTele.append(telefone)
    elif opcao == 'B' or opcao == 'b':
        print(listaNome,'\n')
    elif opcao == 'C' or opcao == 'c':
        consulta = input("Informe o nome do cliente:")
        for i in range(len(listaNome)):
            if listaNome[i] == consulta:
                print(f"""
Nome:{listaNome[i]}
Idade:{listaIdade[i]}
Sexo:{listaSexo[i]}
Telefone:{listaTele[i]}""")
            else:
                print("Cliente não Cadastrado!")
    elif opcao == 'D' or opcao == 'd':
        delete = input("Informe o nome do cliente:")
        for i in range(len(listaNome)):
            if listaNome[i - 1] == delete:
                listaNome.remove(listaNome[i - 1])
                listaIdade.remove(listaIdade[i - 1])
                listaSexo.remove(listaSexo[i - 1])
                listaTele.remove(listaTele[i - 1])
            else:
                print("Cliente Deletado ou Não Cadastrado")
    elif opcao == 'S' or opcao == 's':
        print("Muito obrigado por usar o programa tenha um bom dia!")
        break
    else:
        print("Opção Invalida!")