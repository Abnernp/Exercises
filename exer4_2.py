# 4.2
vel = int(input("Qual a velocidade do carro?: "))
multa = (vel - 80) * 5
if vel > 80:
    print("Você foi multado em", multa,"reais")