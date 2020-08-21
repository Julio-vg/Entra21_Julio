#Execicios 04
#Exercicio retirado do site <https://wiki.python.org.br/EstruturaDeDecisao>
#Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
#Dicas:
#Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#Triângulo Equilátero: três lados iguais;
#Triângulo Isósceles: quaisquer dois lados iguais;
#Triângulo Escaleno: três lados diferentes;

lado1 = int(input("Tamanho do primeiro lado do triangulo:"))
lado2 = int(input("Tamanho do segundo lado do triangulo:"))
lado3 = int(input("Tamanho do terceiro lado do triangulo:"))


if lado1 == lado2 == lado3 and lado2 == lado1 == lado3 and lado3 == lado1 == lado2:
    print("Triângulo Equilátero")

elif lado1 != lado2 == lado3 or lado2 != lado1 == lado3 or lado3 != lado2 == lado1:
    print("Triângulo Isósceles")

elif lado1 != lado2 != lado3 and lado2 != lado1 != lado3 and lado3 != lado2 != lado1:
    print("Triângulo Escaleno")