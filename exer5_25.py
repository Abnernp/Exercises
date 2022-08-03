#5.25
n = int(input("Digite um número: "))
b = 2
while (n - (b * b)) > 0.00001:
    p = (b + (n / b)) / 2
    b = p
print(f"A raiz quadrada de {n} é aproximadamente {p:4.4f}")

