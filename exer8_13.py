#8.13
def funcaovalida(s):
    s = s.lower()
    opcao = ("a", "b")
    if s in opcao:
        return s
    else:
        print("Opção inválida, escolha outra opção!")
    print(funcaovalida(input("Digite uma opção: ")))
print(funcaovalida(input("Digite uma opção: ")))
