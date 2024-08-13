# Usando declaraciones if y else podemos escribir un programa que muestre un saludo si hora es menor que 12 y otro si no cumple la condicion

hora = 9
if hora < 12:
    print ("good morning")

else:
    print ("Good night")  

# Para una condicion mas especifica, como si hour es mayor que 12 pero menor que 17, podemos codificar elif hour <17: en su lugar
# elif significa mas si. elif se usa cuando hay una segunda condicion que debe verificarse cuando no se cumple la condicion de bloque if

hour = 14
if hour < 12:
    print ("Good morning")

elif hour < 17:
    print ("Good afternoon")

# Podemos codificar una declaracion else para ejecutar su bloque de codigo cuando las condiciones if y elif sean false

horas = 18

if hora < 12:
    print ("Good morning")

elif hora < 17:
    print ("Good afternoon")

else:
    print ("Good night")

# Siempre que vayan antes de la declaracion else, podemos agregar tantas declaraciones elif como queramos

hours = 20
if hours < 12:
    print ("Good morning")

elif hours < 17:
    print ("Good afternoon")

elif hours < 21:
    print ("Good evining")

else:
    print ("Good night")

# Muestra un mensaj en la consola cuando topping no es igual a "pineapple" o "pepperoni"

topping = "champiñón"
if topping == "pineapple":
    print ("Solicitud Denegada")

elif topping == "pepperoni":
    print ("Solicitud Denegada")

else:
    print ("No se pudo procesar la solicitud")

# Mostrar Welcome! en la consola cuando edad es mayor que 16 y menor que 100 codificando una segunda declaracion elif

edad = 90

if edad <= 12:
    print ("¿Dónde están tus padres?")

elif edad <= 16:
    print ("Eres demasiado joven para subirte a este paseo")

elif edad < 100:
    print ("Welcome")