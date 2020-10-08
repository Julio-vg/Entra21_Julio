valor=input().split()

a, b, c = valor
pi=3.14159

tri= float(a) * float(c)/2
cir= pi * float(c) * float(c)
tra= float(c) *(float(a) + float(b))/2
qua= float(b) * float(b)
ret= float(a) * float(b)

print("""TRIANGULO: %.3f
CIRCULO: %.3f
TRAPEZIO: %.3f
QUADRADO: %.3f
RETANGULO: %.3f""" % (tri, cir, tra, qua, ret))