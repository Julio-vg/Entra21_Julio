dias = int(input())

anos = dias // 350
dias = dias - anos*365
meses = dias // 30
dias = dias - meses*30
dias = dias

print(f"""{anos} ano(s)
{meses} mes(es)
{dias} dia(s)""")