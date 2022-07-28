#4.9
print("Simulador para compra de imóvel")

valor = float(input("Digite o valor do imóvel: "))
anos = float(input("Digite a quantidade de anos do financiamento: "))
salario = float(input("Digite o valor do salário: "))

tempo = anos * 12
prestacao = valor / tempo

if prestacao > salario * 30 / 100:
    print("Financiamento não aprovado")
else:
    print(f"O valor da prestação será de R${prestacao:6.2f}")