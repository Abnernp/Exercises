#8.12
def string_na_lista(var, lista):
    return var in lista
print(string_na_lista("ab", ["abc",  "abcd", "abcdef", "a"]))
print(string_na_lista("abc", ["abc",  "abcd", "abcdef", "a"]))
print(string_na_lista("nre", ["abc",  "abcd", "abcdef", "a"]))
print(string_na_lista("abcdef", ["abc",  "abcd", "abcdef", "a"]))

