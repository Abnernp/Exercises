#6.6
ultimof1 = 0
ultimof2 = 0
fila1 = list(range(1, ultimof1+1))
fila2 = list(range(1, ultimof2+1))
while True:
    print(f"Existem {len(fila1)} clientes na fila 1")
    print(f"Existem {len(fila1)} clientes na fila 2")
    print("Fila 1 atual:", fila1)
    print("Fila 2 autal:", fila2)
    print("Digite F para adicionar um cliente ao fim da fila 1,")
    print("Digite G para adicionar um cliente ao fim da fila 2,")
    print("Digite A para realizar o atendimento na fila 1,")
    print("Digite B para realizar o atendimento na fila 2,")
    print("Digite S para sair.")
    op = input("Operação (F, G, A, B ou S):")
    x = 0
    sair = False
    while x < len(op):
        if op[x] == "A" or op[x] == "a":
            if len(fila1) > 0:
                atendido = fila1.pop(0)
                print(f"Cliente {atendido} da fila 1 atendido")
            else:
                print("Fila vazia! Ninguém para atender.")
        elif op[x] == "F" or op[x] == "f":
            ultimof1 += 1  # Incrementa o ticket do novo cliente
            fila1.append(ultimof1)
        elif op[x] == "B" or op[x] == "b":
            if len(fila1) > 0:
                atendido = fila2.pop(0)
                print(f"Cliente {atendido} da fila 2 atendido")
            else:
                print("Fila vazia! Ninguém para atender.")
        elif op[x] == "G" or op[x] == "g":
            ultimof2 += 1  # Incrementa o ticket do novo cliente
            fila2.append(ultimof2)
        elif op[x] == "S" or op[x] == "s":
            sair = True
            break
        else:
            print(f"Operação inválida: {op[x]} na posição {x}! Digite apenas F, G, A, B ou S!")
        x = x + 1
    if sair:
        break