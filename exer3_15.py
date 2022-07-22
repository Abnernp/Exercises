# Cálculo de vida de um fumante

c_dia = float(input("Informe quantos cigarros fuma por dia: "))
anos = float(input("Informe quantos anos ja fumou: "))
vida = (anos * 365 * c_dia * 10) / 1440  # 1440 conversão de 1 dia para minutos
print("Perdeu %5.f dias de vida por causa do cigarro" % vida)
