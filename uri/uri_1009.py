nome=input()
salario=float(input())
venda=float(input())

comissao=venda*15/100+salario

print("TOTAL = R$ %.2f" % comissao)