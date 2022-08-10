#6.17
estoque = {"tomate": [100, 2.30],
           "alface": [500, 0.45],
           "batata": [2001, 1.20],
           "feijão": [100, 1.5]}
total = 0
print("Vendas:\n")
while True:
    produto = input("Digite o nome do produto ou (fim) para sair: ")
    if produto == "fim":
        break
    if produto in estoque:
        quantidade = int(input("Digite a quantidade: "))
        if quantidade <= estoque[produto][0]:
            preco = estoque[produto][1]
            custo = preco * quantidade
            print(f"{produto:6s}: {quantidade:3d} x {preco:3.2f} = {custo:4.2f}")
            estoque[produto][0] -= quantidade
            total += custo
        else:
            print("Quantidade indisponível")
    else:
        print("Produto inválido")
print(f"Custo total: {total:19.2f}\n")
print("Estoque:\n")
for chave, dados in estoque.items():
    print("Descrição:", chave)
    print("Quantidade:", dados[0])
    print(f"Preço:{dados[1]:3.2f}\n")