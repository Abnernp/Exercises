#6.2
l1 = []
l2 = []
while True:
    n = int(input("Digite um número para primeira lista ou 0(zero) para sair: "))
    if n == 0:
        break
    l1.append(n)
while True:
    n = int(input("Digite um número  para segunda lista ou 0(zero) para sair: "))
    if n == 0:
        break
    l2.append(n)
l3 = l1[:]
l3.extend(l2)
print("A união das listas", l3)