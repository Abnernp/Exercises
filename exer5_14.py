#5.14
s = 0
x = 0
while True:
    v = int(input("Digite um número para somar ou 0 para sair: "))
    x += 1
    if v == 0:
        break
    s += v
print(f"Foram digitados {x-1} números diferentes")
print(f"A soma deles é: {s}")
print(f"A média é {s/(x-1):2.2f}")