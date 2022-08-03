#5.9
n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))
x = n1
result = 0
while x >= n2:
    result = result + 1
    x = x - n2
resto = x
print(f"{n1} / {n2} = {result} (resto) {resto}")