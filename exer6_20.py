#6.20
l1 = [1, 2, 3, 4, 5, 7]
l2 = [3, 4, 6, 8, 9]

a = set(l1)
b = set(l2)
print(l1)
print(l2)
print("Elementos que não mudaram:", a & b)
print("Novos elementos:", b - a)
print("Elementos removidos:", a - b)