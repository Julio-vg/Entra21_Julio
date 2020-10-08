#  Exercicio 20
# Usando a seguinte fórmula:
# 
# valor_receber = dinheiro_emprestado*(1+(taxa_juros/100))**tempo_emprestimo
# 
# Crie um programa que solicite ao usuário o valor do dinheiro emprestado, 
# a taxa de juros em porcentagem e o tempo do empréstimo.
# 
# Mostre na telas o valor do dinheiro emprestado, a taxa de juros em porcentagem, 
# tempo do empréstimo e o valor que deve ser devolvido no final do empréstimo.

din_emp = float(input("Informe o valor do empréstimo:"))
juros = float(input("Informe o valor de juros:"))
tempo = int(input("Informe o tempo do empréstimo:"))

valor_receber = din_emp*(1+(juros/100))**tempo
print("Valor do empréstimo:", din_emp,"Reais","\nTaxa de juros:", juros,"%","\nTempo do empréstimo:", tempo,"Meses","\nTotal a ser devolvido:", valor_receber,"Reais")



