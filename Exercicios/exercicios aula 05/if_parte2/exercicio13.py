# Exercicio 13
# 
# Crie um programa que peça o nome do cliente, idade, endereço, email e telefone.
# 
# Depois crie um menu interativo com as seguintes opções: Dados, Endereço, Contato.
# 
# Se o usuário selecionar "Dados" deve aparecer o nome do cliente e a idade
# 
# Se o usuário selecionar "Endereço" deve aparecer o nome do cliente e o endereço
# 
# Se o usuário selecionar "Contato" deve aparecer o nome do cliente, email e o telefone

nome = input("Informe o seu nome:")
idade = input("Informe a sua idade:")
endereco = input("Informe seu endereço:")
email = input("Informe seu email:")
fone = input("Telefone para contato:")

menu = """Opções disponiveis
1) Dados
2) Endereço
3) Contato

Escolha uma opção:"""

opcao = input(menu)
if opcao == '1':
    print('Nome:',nome,'Idade:',idade,'Anos.')
elif opcao == '2':
    print('Nome:',nome,'Endereço:',endereco)
elif opcao == '3':
    print('Nome:',nome,'Email:',email,'Telefone:',fone)
else:
    print("Opção Invalida!")




