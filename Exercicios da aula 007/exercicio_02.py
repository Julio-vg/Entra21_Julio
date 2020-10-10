def divisao():

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    if num1 == 0 or num2 == 0:
        print("Não é possivel dividir por zero.")
    else:
        resultado = num1 / num2
        print(f"A divisão entre os números {num1} e {num2} é: {resultado}")
divisao()