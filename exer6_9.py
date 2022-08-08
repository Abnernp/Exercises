#6.9
L = [15, 7, 27, 39]
p = int(input("Digite o valor a procurar: "))
v = int(input("Digite o outro valor a procurar: "))
x = 0
achouP = False
achouV = False
primeiro = 0
while x < len(L):
    if L[x] == p:
        achouP = True
        if not achouV:
            primeiro = 1
    if L[x] == v:
        achouV = True
        if not achouP:
            primeiro = 2
    x += 1
if primeiro == 1:
   print(f"{p} foi achado antes")
elif primeiro == 2:
    print(f"{v} foi achado antes")
else:
    print("Nenhum valor encontrado")