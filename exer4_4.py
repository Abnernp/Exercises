# 4.4
salario = float(input("Qual o valor do salário?: "))
if salario > 1250:
    print(f"O aumento será de R${salario * 10 / 100:6.2f}")
if salario < 1250:
    print(f"O aumento será de R${salario * 15 / 100:6.2f}")