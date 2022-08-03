#5.8
n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))
x = 1
result = 0
while x <= n2:
    result = result + n1
    x = x + 1
print(f"{n1} x {n2} = {result}")