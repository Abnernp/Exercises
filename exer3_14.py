# Cálculo do preço de carro de aluguel

km = float(input("Digite a quantidade de Km percorridos: "))
dias = int(input("Digite a quantidade de dias de uso: "))
d = dias * 60
kmr = km * 0.15
print("Custo total da viagem foi de R$", d + kmr, "reais")
