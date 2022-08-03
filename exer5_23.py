#5.23
n = (int(input("Digite um número: ")))
if n < 0:
    print("Digite apenas números positivos")
elif n == 0 or n == 1:
    print(f"{n} não é primo")
elif n > 1:
    for i in range(2, n):
        if n % i == 0:
            print(n, 'não é primo')
            break
    else:
        print(n, 'é primo')