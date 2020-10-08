"""Exercício 2

(não usar o continue ou o break)

Crie um menu interativo com as seguintes opções:

A) soma
B) Média
C) Taboada
S) Sair


Para A: Peça 2 números, some e mostr o resultado
Para B: Peça 4 números, faça a média e mostre o resultado
Para C: Peça um número e mostre a taboada dele
Para S: Mostre uma mensagem de despidida e encerre o programa.
Para qualquer outro valor: Mostre a mensagem "opção inválida"""

opcao = ''
medialista = []
while opcao != 'S':
    opcao = input("""Menu de oprações matematicas:
    A) Soma:
    B) Média:
    C) Taboada:
    S) Sair
    
    Digite a opção desejada:""")

    print("\n")
    if opcao == 'A':
        num1 = int(input("Digite o primeiro número:"))
        num2 = int(input("Digite o segundo número:"))
        print(f"Resultado:{num1+num2}\n")
    elif opcao == 'B':
        for i in range(4):
            opcao = int(input(f"Digite o numero {i+1}:"))
            medialista.append(opcao)
        print(f"Resultado:{sum(medialista)/len(medialista)}\n")
    elif opcao == 'C':
        opcao = int(input("Digite um número:"))
        for i in range(11):
            print(f"{opcao} X {i} = {opcao*i}\n")
    elif opcao == 'S':
        print("Obrigado por usar o programa.")
    else:
        print("Opção Invalida!")

