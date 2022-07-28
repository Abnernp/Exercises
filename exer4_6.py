# 4.6
dist = float(input("Digite a distância da viagem: "))
if dist < 200:
    print(f"O valor da passagem é R$ {0.5 * dist:4.2f}")
else:
    print(f"O valor da passagem é R$ {0.45 * dist:4.2f}")