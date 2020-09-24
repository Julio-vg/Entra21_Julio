maior = input().split()

a, b, c = maior

cal1 = (int(a) + int(b) + abs(int(a) - int(b)))/2
resultado = (cal1 + int(c) + abs(cal1 - int(c)))/2

print("%d eh o maior" % resultado)