#4.7
c = int(input("Digite  categoria do produto: "))
if c == 1:
    p = 10
else:
    if c == 2:
        p = 18
    else:
        if c == 3:
            p = 23
        else:
            if c == 4:
                p = 26
            else:
                if c == 5:
                    p = 31
                else:
                    print("Categoria inválida, digite um valor entre 1 e 5 !")
                    p = 0
print(f"O preço do produto é: R${p:2.2f}")