import itertools
import string
import random

caracteres = string.ascii_letters + string.digits + string.punctuation
combinaciones = itertools.product(caracteres, repeat=6)

mi_diccionario = {}
for combinacion in combinaciones:
    clave = "".join(combinacion)
    valor = ''.join(random.choices(caracteres, k=10))
    mi_diccionario[clave] = valor

print(mi_diccionario)
