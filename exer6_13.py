#6.13
t = [-10, -8, 0, 1, 2, 5, -2, -4]
minimo = t[0]
maximo = t[0]
x = 0
for e in t:
    if e < minimo:
        minimo = e
    if e > maximo:
        maximo = e
    x = x + e
media = x / len(t)
print("Temperatura mínima é", minimo)
print("Temperatura máxima é",maximo)
print("Temperatura média é",media)