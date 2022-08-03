#5.22
while True:
    print("1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n5 - Sair")
    a = int(input("Digite a opção desejada: "))
    if a == 5:
        break
    elif a >= 1 and a < 5:
        n = int(input("Tabuada de: "))
        x = 1
        while x <= 10:
            if a == 1:
                print(f"{n} + {x} = {n + x}")
            elif a == 2:
                print(f"{n} - {x} = {n - x}")
            elif a == 3:
                print(f"{n} x {x} = {n * x}")
            elif a == 4:
                print(f"{n} / {x} = {n / x:5.2f}")
            x = x + 1
    else:
        print("Opção inválida!")