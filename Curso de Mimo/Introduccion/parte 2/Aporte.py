print ("what is you name")
name_input = input()
print (f"Hi, {name_input}")

# Para recopilar informacion de un usuario en programa python, se usa la funcion inpu(). luego la entreda del usuario se puede asignar a una variable
 
user_input = input()

# Tambien podemos agregar un mensaje adicional a la funcion input()

user = input("enter you name")

# Si ingresamos un mensaje adicional, el usuario comenzara a escribir en la misma linea en la que muestra el mensaje en la consola
# Por eso es util agregar un epacio  en blancoal final de la consola utilizado la funcion input

usuario = input(" escriba su nombre ")
print (f"gracias, {usuario}")

# Podemos usar la funcion input tantas veces como queramos

usuario1 = input(" Enter numero ")
usuario2 = input(" Enter numero ")
print (usuario1)
print (usuario2)

# La entreda es siempre de tipo string. Si queremos usarlo como un numero, debemos covertilo a un numero entero o flotante de antemano

user1 = input (" escriba un numero ")
user2 = input (" escriba otro numero ")

number1 = int(user1)
number2 = int (user2)

result = number1 + number2
print (f" the sum is {result}")
