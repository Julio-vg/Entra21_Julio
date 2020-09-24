A, B, C = input().split()

A = float(A)
B = float(B)
C = float(C)

X = (B**2) - (4*A*C)

if A == 0 or X < 0:
    print("Impossivel calcular")
else:
    x1 = (- B + X **(1/2))/(2*A)
    x2 = (- B - X **(1/2))/(2*A)
    print("R1 = %.5f" % x1)
    print("R2 = %.5f" % x2)

