#6.18
frase = input("Digite uma frase para montar um dicionário: ")
dicionario = {}
for letra in frase:
   dicionario[letra] = dicionario.get(letra, 0 ) + 1
print(dicionario)