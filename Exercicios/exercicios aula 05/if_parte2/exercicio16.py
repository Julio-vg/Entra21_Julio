# Exercicio 16
# 
# Crie um programa para uma promoção de um posto de combustivel.
# 
# O programa deve pedir ao usuário quantos litros ele quer abastecer e qual combustivel: álcool, diessel ou gasolina
# 
# A promoção é a seguinte:
#  - Para gasolina: Até 20 litros 0% de desconto e acima de 20 litros 10% de desconto
#  - Para diessel: Até 10 litro 1.5% de desconto e acima de 10 litros 5% de desconto
#  - para álcool: Até 10 litros 5% de desconto e acima de 10 litros 10% de desconto.
#  
# Mostre o combustivel que ele selecionou, o total abastecido e a porcentagem de desconto a ser aplicada.
# 
# Não precisa calcular o valor do combustivel!
# 
litros = int(input("Quantos Litros Você Deseja Colocar:"))
comb = input("Qual combustivel você deseja Alcool,Diessel ou Gasolina:")

if litros <= 20 and comb == 'Gasolina':
    print("Tipo:", comb,"-", litros,"Litros","-","0% de Desconto.")
elif litros > 20 and comb == 'Gasolina':
    print("Tipo:", comb,"-", litros,"Litros","-","10% de Desconto.")
elif litros <= 10 and comb == 'Diessel':
    print("Tipo:", comb,"-", litros,"Litros","-","1.5% de Desconto.")
elif litros > 10 and comb == 'Diessel':
    print("Tipo:", comb,"-", litros,"Litros","-","5% de Desconto.")
elif litros <= 10 and comb == 'Alcool':
    print("Tipo:", comb,"-", litros,"Litros","-","5% de Desconto.")
elif litros > 10 and comb == 'Alcool':
    print("Tipo:", comb,"-", litros,"Litros","-","10% de Desconto.")
else:
    print("Opção Invalida!")

