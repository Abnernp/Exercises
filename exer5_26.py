#5.26
n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número para dividir o primeiro: "))
div = 0
x = n1
while x >= n2:
    x = x - n2
    div = div + 1
resto = x
print(f"O resto da divisão de {n1} / {n2} \né {resto}")