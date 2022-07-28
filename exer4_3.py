# 4.3
a = float(input("Digite um número: "))
b = float(input("Digite outro número: "))
c = float(input("Digite mais um número: "))

if a > b and a > c:
    print("O maior é:", a)
if b > a and b > c:
    print("O maior é:", b)
if c > a and c > b:
    print("O maior é:", c)
if a < b and a < c:
    print("O menor é:", a)
if b < a and b < c:
    print("O menor é:", b)
if c < a and c < b:
    print("O menor é:", c)