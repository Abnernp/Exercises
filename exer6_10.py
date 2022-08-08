#6.10
L = [15, 7, 27, 39]
p = int(input("Digite o valor a procurar: "))
v = int(input("Digite o valor a procurar: "))
x = 0
y = 0
while x < len(L):
    if L[x] == p:
        print(f"{p} achado na posição {x+1}")
        break
    x += 1
else:
    print(f"{p} não encontrado")
while y < len(L):
    if L[y] == v:
        print(f"{v} achado na posição {y+1}")
        break
    y += 1
else:
    print(f"{v} não encontrado")