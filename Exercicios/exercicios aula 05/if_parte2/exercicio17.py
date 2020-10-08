# Exercicio 17
# crie um programa que peça 4 notas de um aluno e calcule a média "(nota1+nota2+nota3+nota4)/4" e retorne:
# 
# Pra média igual a 10 apareça a mensagem "Aprovado com louvor"
# Pra média maior igual a 7 apareça a mensagem "Aprovado"
# Pra média menor que 7 apareça a mensagem "Reprovado"
# 
nota1 = int(input("Informe a primeira nota do aluno:"))
nota2 = int(input("Informe a segunda nota do aluno:"))
nota3 = int(input("Informe a terceira nota do aluno:"))
nota4 = int(input("Informe a quarta nota do aluno:"))

media = (nota1 + nota2 + nota3 + nota4)/4

if media == 10:
    print("Aluno Aprovado com Louvor!")
elif media >= 7:
    print("Aluno Aprovado!")
elif media < 7:
    print("Aluno Reprovado!")