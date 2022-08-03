#5.7
print("Selecione a tabuada")
n = int(input("Tabuada de: "))
x = int(input("Primeiro múltiplo sendo: "))
y = int(input("Último múltiplo sendo: "))
while x <= y:
    print(f"{n} X {x} = {n * x}")
    x = x + 1