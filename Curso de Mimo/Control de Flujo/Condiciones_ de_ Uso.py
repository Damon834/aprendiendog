# Podemos utilizar operadores de comparacion en programas para comprobar si la answer a una pregunta es correcta
# Escribir == para comparar la solucion esperada con la respuesta dada

answer = "picaso"
if answer == "picaso":
    print (answer + " is correct")

# ¿Que pasa si la respuesta del cuestionario de tria no es correcta? se usa != para verificar anwer no es igual picasso

anwer = "Matisse"
if answer != "picasso":
    print (anwer + " is wrong")

# Podemos almacenar el resultado de una comparacion en una variable 

score = 51
pass_grade = score > 50
if pass_grade:
    print ("passed")

# Codifique una condicion que ejecute el codigo si replay_times es mayor o igual a 300

song = "Dont not stop me now"
replay_times = 345

if replay_times >= 300:
    print ("Your top song this week: ")
    print (song)

# Codifique una condicion para sugerir un restaurante si la dieta del usuario es vegetaliana

dieta = "Vegetaliana"
Restaurante_Vegetaliano = "Root"
Restaurante = "DelPosto"

if dieta == "Vegetaliana":
    print ("Try out")
    print (Restaurante_Vegetaliano)

# Uttilizar >= para escribir una condicion que verifique si la edad del usuario es mayor o igual a 18

edad = 20
can_drive = False

if edad >= 18:
    can_drive = True

print(can_drive)

# Almacenar la comparacion de igualdad entre inbox_full y True dentro show_alert

inbox_full = True
show_alert = inbox_full == True

if show_alert:
    print ("Inbox full")
    print ("Archive some to continue")

# Actualice la variable suscribete para que la condicion se True y el texto se muestre en la consola 

suscribete = False
suscribete = True

if suscribete:
    print ("Gracias por susbribirte")

# Codifique una sentencia if que utilice > comparacion para ejecutar codigo si escore es mayor que un numero

escore = 100
if escore > 50:
    print("New highest escore")

# En la primera condicion, verifique si grade no es igual "A" En la segunda condicion verifique si subject es igual a "Math"

subject = "Math"
grade = "A"

if grade != "A":
    print (f"Give {subject} a chance")

if subject == "Math":
    print ("Today's a great day for solving equations!")

# Utilice < para escribir una condicion que verifique si carbon_level es inferior a 300

carbon_level = 200
if carbon_level < 300:
    print (f"{carbon_level} ppm is not enough co2 for photosynthesis")