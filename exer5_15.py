#5.15
s = 0
while True:
    cod = int(input("Digite o código do produto ou Zero(0) para sair: "))
    if cod == 0:
        break
    if cod == 1:
        preco = 0.5
    elif cod == 2:
        preco = 1
    elif cod == 3:
        preco = 4
    elif cod == 5:
        preco = 7
    elif cod == 9:
        preco = 8
    else:
        print("Código inválido!")
        cod = int(input("Digite o código do produto ou Zero(0) para sair: "))
    q = int(input("Digite a quantidade: "))
    x = preco * q
    s = s + x
print(f"Total das compras R$ {s:2.2f}")
