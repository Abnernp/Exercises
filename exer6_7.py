#6.7
seq = input("Digite a sequência de parênteses a validar: ")
x = 0
pilha = []
while x < len(seq):
    if seq[x] == "(":
        pilha.append("(")
    if seq[x] == ")":
        if len(pilha) > 0:
            topo = pilha.pop(-1)
        else:
            break
    x = x + 1
if len(pilha) == 0:
    print("Válida")
else:
    print("Erro")