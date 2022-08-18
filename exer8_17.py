#8.17
def geradorfibonacci():
    p = 0
    s = 1
    y = int(input("Digite o último número pra sequência fibonacci: "))
    while s < y:
        yield s
        p, s = s, s + p
print([x for x in geradorfibonacci()])