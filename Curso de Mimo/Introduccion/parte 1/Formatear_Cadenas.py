# Aprendimos que podemos usar + para agregar dos cadenas y mostralas juntas

print ( "new" + "messages")

# Las cadenas f, abreviatura de caddenas formateadas, nos permiten mostar expresiones como agregar a un string a un numero
# sin ningun error ( la f no puede estar separda de la comilla)

print ( f" {2} nuevo mensaje")
print (f" {8} Nuevos Mensajes ")

# Insertar variables como new_messages entre llaves tambien muestra su valor

new_messages = 2 
print (f"{new_messages} new messages")

# Tambien podemos usar expresiones como new - read entre llaves para mostar su valor

new = 5 
read  = 2
print (f"{ new - read} unread messages")

# Podemos usar llaves para insertar valores tantas veces como queramos dentro de la cadena f 

print (f"{5} Mensajes y {3} Amigos" )

# Para utilizar una cadena f, podemos guardala en una variable

nuevo = 5
estados = f"{new} texto"
print ( estados)

# Muestre la temperatura actual codificando degress entre llaves 

degress = 70
print (f"Temperatura: {degress} F")

# Guarde la cadena f en la display de variable

movie = " Vertigo "
display = f" Airing tonight:{movie} "
print (display)


