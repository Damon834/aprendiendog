first_counter = 0
while first_counter < 5:
    print ("**********---------")
    first_counter += 1

second_counter = 0
while second_counter < 4:
    print ("-------------------")
    second_counter += 1

# Usando bucles fo, podemos escribir programas con mucho menos codigo 

for i in range (4):
    print ("**********---------")

for i in range (4):
    print ("-------------------")

# La variable anterior in, en este caso i es la variable contador. Cuenta en que repeticion de bucle nos encongtramos 

for i in range (3):
    print (i)
    print ("For loops are great!")

# Dentro de del bucle for, muestre el valor de la variable contador

for x in range (5):
    print ("Round")
    print (x)

# Dentro del bloque de codigo del bucle for agregue ~ a la variable line usando el operador +=

print ("*")
line = ""
for i in range (4):
    line += "~"
    print (line)