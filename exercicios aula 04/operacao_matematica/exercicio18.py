# Exercicio 18
# Crie um programa que solicite o valores (inteiros) de a, b e c para o cálculo do delta
# 
# A fórmula do delta é:
# 
# delta = b²-4ac
# 
# após calcular, mostre o resultado na tela.

b = int(input("Informe o valor de b:"))
a = int(input("Informe o valor de a:"))
c = int(input("Informe o valor de c:"))

delta = b*b - 4*a*c
print("Resultado:", delta)