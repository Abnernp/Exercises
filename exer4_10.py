#4.10
print("Cálculo da fatura de energia")
q = float(input("Digite a quantidade de kWh consumida no mês: "))
tipo = int(input("Digite o tipo de instalação, (1) residências, (2) indústrias, (3) comércios: "))
if tipo == 1 and q <= 500:
    print(f"O valor da fatura é R$ {0.40 * q:6.2f}")
elif tipo == 1 and q > 500:
    print(f"O valor da fatura é R$ {0.65 * q:6.2f}")
elif tipo == 2 and q <= 1000:
    print(f"O valor da fatura é R$ {0.55 * q:6.2f}")
elif tipo == 2 and q > 1000:
    print(f"O valor da fatura é R$ {0.60 * q:6.2f}")
elif tipo == 3 and q <= 5000:
    print(f"O valor da fatura é R$ {0.55 * q:6.2f}")
elif tipo == 3 and q > 5000:
    print(f"O valor da fatura é R$ {0.60 * q:6.2f}")
else:
    print("Digite um tipo válido!")