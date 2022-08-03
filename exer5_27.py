#5.27
n = input("Digite um número: ")
if n == n[::-1]:
    print(n, "é palíndromo!")
else:
    print(n, "não é palíndromo!")