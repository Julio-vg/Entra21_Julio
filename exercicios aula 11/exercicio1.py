"""Exercício 1

(não usar o continue ou o break)

Crie um programa que mostre um memu com as seguites opções:

1) Soma
2) Subtração
3) Multiplicação
S) Para sair!

Para número 1: Peça 2 números e mostre a soma deles
Para número 2: Peça 2 númeors e mostre a subtração deles
Para númeor 3: Peça 2 números e mostre a multiplicação deles
Para S: Mostre uma mensagem de despedida e termine o programa.

Para qualquer outra opção deve aparecer a mensagem "Opção Inválida"
"""

opcao = ''

while opcao != 'S':
    opcao = input("""Programa de Operações Matematicas:
    1) Soma
    2) Subtração
    3) Multiplicação
    S) Sair!
    Digite a opção Desejada:""")

    print("\n")
    if opcao == '1':
        num1 = int(input("Digite o primeiro número para soma:"))
        num2 = int(input("Digite o segundo número para soma:"))
        print(f"Resultado:{num1 + num2}\n")
    elif opcao == '2':
        num1 = int(input("Digite o primeiro número para subtração:"))
        num2 = int(input("Digite o segundo número para subtração:"))
        print(f"Resultado:{num1 - num2}\n")
    elif opcao == '3':
        num1 = int(input("Digite o primeiro número para multiplicação:"))
        num2 = int(input("Digite o segundo número para multiplicação:"))
        print(f"Resultado:{num1 * num2}\n ")
    elif opcao == 'S':
        print("Obrigado por usar o programa.\n")
    else:
        print("Opção Invalida!\n")