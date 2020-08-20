# Exercicio 12
# 
# Crie um programa que peça 2 números.
# 
# Depois mostre um menu interativo contendo 5 operações matemáticas do python
# (adição, subtração, multiplicação, divisão e expoente)
# 
# Peça para o usuário escolher uma destas opções e mostre o resultado da operação escolhida.

num1 = int(input("Digite um número:"))
num2 = int(input("Digite outro número:"))

mensagem = """Operações matematicas:
1) Adição
2) Subtração
3) Multiplicação
4) Divisão
5) Expoente

Escolha uma operação:"""

opcao = input(mensagem)

if opcao == '1':
    print("Resultado:", num1 + num2)
elif opcao == '2':
    print("Resultado:", num1 - num2)
elif opcao == '3':
    print("Resultado:", num1 * num2)
elif opcao == '4':
    print("Resultado:", num1 / num2)
elif opcao == '5':
    print("Resultado:", num1 ** num2)
else:
    print("Opção Invalida!")








