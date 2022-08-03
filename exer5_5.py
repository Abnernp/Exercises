#5.5
print("Primeros múltiplos de 3")
fim = int(input("Digite o último número a imprimir: "))
x = 1
while x<= fim and x <= 30:
    if x % 3 == 0:
        print(x)
    x = x + 1