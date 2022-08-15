#8.11
def faixa_string(pergunta, minimo, maximo):
    tamanho = len(pergunta)
    return minimo <= tamanho <= maximo
print(faixa_string("abc", 1, 5))
print(faixa_string("abcde", 2, 3))
print(faixa_string("ab", 3, 5))
print(faixa_string("123456", 1, 10))