#Execicios 02
#Escreva um programa que receba 4 notas e calcule a média.
# Mostre a seguinte mensagem conforme a media final.
#Media Final
#de 0 a 5 - Reprovado
#de 5 a 6.5 - Recuperação
#de 6.5 a 9 - Aprovado
#Acima de 9 - Aprovado com louvor
#fórmula:(nota1+nota2+nota3+nota4)/4

nota1 = float(input("Informe a primeira nota do aluno:"))
nota2 = float(input("Informe a segunda nota do aluno:"))
nota3 = float(input("Informe a terceira nota do aluno:"))
nota4 = float(input("Informe a quarta nota do aluno:"))

media_final = (nota1 + nota2 + nota3 + nota4)/4

if media_final >= 0 and media_final <= 5:
    print("Aluno Reprovado!")

elif media_final >= 5 and media_final <= 6.5:
    print("Aluno em recuperação!")

elif media_final > 6.5 and media_final <= 9:
    print("Aluno Aprovado!")

elif media_final > 9:
    print("Aluno Aprovado com Louvor!")

