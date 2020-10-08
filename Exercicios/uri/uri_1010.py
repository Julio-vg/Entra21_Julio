a=input().split()
b=input().split()

peca1, numero1, valor1 = a
peca2, numero2, valor2 = b

total = (int(numero1) *float(valor1)) + (int(numero2) * float(valor2))

print("VALOR A PAGAR: R$ %.2f" % total)