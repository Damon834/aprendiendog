import string
import random

def GeneradorClave ( tamaño = 10, caracteres = string.ascii_letters + string.digits + string.punctuation ):
    return ''.join (random.choice (caracteres) for _ in range (tamaño) ) 

print (GeneradorClave())

def Claves ( tamaño  = 12, caracteres = string.ascii_letters ):
    return ''.join (random.choice (caracteres) for _ in range (tamaño))

print (Claves()) 

def passaword  ( tamaño = 14, caracteres = string.digits ):
    return ''.join (random.choice (caracteres) for _ in range (tamaño))

print (passaword())

def contraseñas ( tamaño = 15, caracteres = string.punctuation ):
    return ''.join (random.choice (caracteres) for _ in range (tamaño))

print (contraseñas())
