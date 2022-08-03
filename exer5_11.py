#5.11
dep = float(input("Digite o valor do depósito inicial: "))
taxa = float(input("Digite a taxa de juros da poupança: "))
x = 1
t = taxa * dep / 100
total = t + dep
while x <= 24:
    print(total)
    total = total + t
    x = x + 1
print(f"O valor após 2 anos é R$ {total:2.2f}")
