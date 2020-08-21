#Escreva um programa que contenha um menu com 4 opções:
#A) soma
#B) média
#C) divisão
#D) Sair
#As opções podem ser escolhidas com as letras maiusculas ou minusculas.
#Para a opção soma, deve solicitar 2 números, fazer a soma e mostrar o resultado.
#Para a opção média, deve solicitar 4 números, fazer a média e mostrar os resultados.
#Para a opção divisão, deve solicitar 2 números, dividir o primeiro pelo segundo e montrar o resultado. Caso o segundo for igual a 0, então deve mostrar o a mensagem "Erro! Não pode dividir por ZERO!"
#Para a opção sair, deve aparecer a mensagem: "Muito Obrigado e Volte sempre!"
menu = """Programa de operações matematicas
A) Soma
B) Média
C) Divisão
D) Sair

 Escolha qual opração voçê desejar utilizar:"""
opcao = input(menu)

if opcao == 'a' or opcao == 'A':
     num1 = int(input("Digite um número:"))
     num2 = int(input("Digite outro número:"))

     print("Resultado da opração:", num1 + num2)

elif opcao == 'b' or opcao == 'B':
    num3 = int(input("Digite o primeiro número:"))
    num4 = int(input("Digite o segundo número:"))
    num5 = int(input("Digite o terceiro número:"))
    num6 = int(input("Digite o quarto número:"))

    print("Resultado da operação:", (num3 + num4 + num5 + num6)/4)

elif opcao == 'c' or opcao == 'C':
    num7 = float(input("Digite um número:"))
    num8 = float(input("Digite outro número:"))
    if num7 == 0 or num8 == 0:
        print("Não é possivel dividir por ZERO!!!!")
    else:
        print("Resultado da operação:", num7 / num8)

elif opcao == 'd' or opcao == 'D':
    print("Obrigado e Volte Sempre!")

else:
    print("Opção Invalida!!")
