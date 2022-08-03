#5.13
divida = float(input("Informe o valor da dívida: "))
taxa = float(input("Informe a taxa de juros mensal: "))
pagamento = float(input("Informe o valor a ser pago por mês: "))
mes = 1
saldo = divida
j_pago = 0
while saldo > pagamento:
    juros = saldo * taxa / 100
    saldo = saldo + juros - pagamento
    j_pago = j_pago + juros
    mes = mes + 1
print(f"O juros ficará em {j_pago:2.2f}, você levará {mes} meses para quitar, sendo que a última parcela será de {saldo:2.2f} e o valor total será de R$ {(divida+j_pago):2.2f}")
