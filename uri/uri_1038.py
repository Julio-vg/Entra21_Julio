item, quant = input().split()

item = int(item)
quant = int(quant)

if item == 1:
    total = quant*4
    print("Total: R$ %.2f" % total)
elif item == 2:
    total = quant*4.50
    print("Total: R$ %.2f" % total)
elif item == 3:
    total = quant*5
    print("Total: R$ %.2f" % total)
elif item == 4:
    total = quant*2
    print("Total: R$ %.2f" % total)
elif item == 5:
    total = quant*1.50
    print("Total: R$ %.2f" % total)