#6.19
l1 = [1, 2, 3, 4, 5, 7]
l2 = [3, 4, 6, 8, 9]

a = set(l1)
b = set(l2)
print(l1)
print(l2)
print("Valores comuns:", a & b)
print("Valores exclusivos na primera:", a - b)
print("Valores exclusivos na segunda:", b - a)
print("Valores não repetidos:", a | b)
print("Primeira lista, sem os elementos repetidos na segunda:", a - b)