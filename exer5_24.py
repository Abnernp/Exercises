#5.24
inicio = 2
n = (int(input("Digite um número: ")))
if n < 0:
    print("Digite apenas números positivos")
else:
    print("Os números primos até:", n)
for i in range(inicio, n + 1):
    if i > 1:
        for j in range(2, i):
            if (i % j == 0):
                break
        else:
            print(i)


