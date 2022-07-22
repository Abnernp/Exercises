# Desconto na marcadoria

mercadoria = float(input("Digite o valor da mercadoria: "))
desconto = float(input("Digite a porcentagem de desconto: "))
valor = mercadoria * desconto / 100
final = mercadoria - valor
print("O valor da mercadoria com desconto é de:", final)
