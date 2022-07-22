# Conversão de dias, horas, minutos e segundos para segundos

dias = float(input("Digite a quantidade de dias: "))
d = dias * 86400
horas = float(input("Digite a quantidade de horas: "))
h = horas * 3600
minutos = float(input("Digite a quantidade de minutos: "))
m = minutos * 60
s = float(input("Digite a quantidade de segundos: "))
print("O total em segundos é: ", d + h + m + s)
