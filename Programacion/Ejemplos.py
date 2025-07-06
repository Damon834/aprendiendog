#suma_total = 0

#for i in range(10):
    #numero = float(input(f"Ingrese el número {i + 1}: "))
    #suma_total += numero

#print("La suma total de los 10 números es:", suma_total)

nume1 = int(input("Ingrese el primer numero: "))
nume2 = int(input("Ingrese el segundo numero: "))

suma = nume1 + nume2
resta = nume1 - nume2
multiplicacion = nume1 * nume2

if nume2 != 0:
    division = nume1 / nume2
    print( "Division:", division)
else:
    print("No se puede dividir por cero.")

print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)


