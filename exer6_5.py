#6.5
ultimo = 10
fila = list(range(1, ultimo+1))
while True:
    print(f"\nExistem {len(fila)} clientes na fila")
    print("Fila atual:", fila)
    print("Digite F para adicionar um cliente ao fim da fila,")
    print("ou A para realizar o atendimento. S para sair.")
    op = input("Operação (F, A ou S):")
    x = 0
    sair = False
    while x < len(op):
        if op[x] == "A" or op[x] == "a":
            if len(fila) > 0:
                atendido = fila.pop(0)
                print(f"Cliente {atendido} atendido")
            else:
                print("Fila vazia! Ninguém para atender.")
        elif op[x] == "F" or op[x] == "f":
            ultimo += 1  # Incrementa o ticket do novo cliente
            fila.append(ultimo)
        elif op[x] == "S" or op[x] == "s":
            sair = True
            break
        else:
            print(f"Operação inválida: {op[x]} na posição {x}! Digite apenas F, A ou S!")
        x = x + 1
    if sair:
        break