#6.8
L = [15, 7, 27, 39]
p = int(input("Digite o valor a procurar: "))
x = 0
while x < len(L):
    if L[x] == p:
        print(f"{p} achado na posição {x+1}")
        break
    x += 1
else:
    print(f"{p} não encontrado")