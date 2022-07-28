#4.8
n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))
op = int(input("Qual operação deseja usar?: soma(1), subtraçào(2), multiplicação(3), ou divisão(4)"))

if op == 1:
    print("O resultado da soma é:", n1 + n2)
elif op == 2:
    print("O resultado da subtração é:", n1 - n2)
elif op == 3:
    print("O resultado da multiplicação é:", n1 * n2)
elif op == 4:
    print("O resultado da divisão é", n1 /n2)
else:
    print("Digite um operador válido!")