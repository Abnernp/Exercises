#6.11
L = []
while True:
    n = int(input("Digite um número ou 0(zero) para sair: "))
    if n == 0:
        break
    L.append(n)
for x in L:
    print(x)