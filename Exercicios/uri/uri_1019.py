tempo = int(input())

horas = tempo // 60**2
tempo = tempo - horas*60**2
minutos = tempo // 60
tempo = tempo - minutos*60
segundos = tempo

print(f"{horas}:{minutos}:{segundos}")