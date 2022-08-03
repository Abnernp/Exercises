#5.12
dep = float(input("Digite o valor do depósito inicial: "))
taxa = float(input("Digite a taxa de juros da poupança: "))
depmensal = float(input("Digite o valor do depósito mensal: "))
x = 1
t = taxa * dep / 100
total = t + dep
dm = depmensal * taxa / 100 + depmensal
while x <= 24:
    print(total)
    total = total + t + dm
    x = x + 1
print(f"O valor após 2 anos é R$ {total:2.2f}")