import string
import random

def cts ( tamaño = 10, caracteres = string.ascii_letters ):
    return ''.join (random.choice (caracteres) for _ in range (tamaño) ) 

for i in range (4):
    print (cts())