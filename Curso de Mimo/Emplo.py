import string
import random

def Claves (tamanio = 10, caracter = string.ascii_letters + string.digits):
    return ''.join (random.choice (caracter) for _ in range (tamanio))

for _ in range (5):
    print (Claves(6))