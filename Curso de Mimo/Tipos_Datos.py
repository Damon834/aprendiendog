# Si no estamos seguro de un tipo de valor podemos comprobarlo aqui, type() comprueba que is_ready sea un booleano (bool)

is_ready = True
print (type(is_ready))

# Podemos obtener rl tipo de variable usando type() con el nombre de la variable. Al agregar print(), podemos ver el tipo de variable en la consola

esta_ready = True
fuel_deposit = 59.80
best_grago = "A"
number_of_pets = 2
print (type(esta_ready))
print (type(fuel_deposit))
print (type(best_grago))
print (type(number_of_pets))

# Python tiene funciones integradas para convertir tipos de datos. Por ejemplo, int() nos ayuda a convertir elalor de un sting
# de la variable age en un numero entero

age = "20"
print (type(age))

convierte_edad = int(age)
print (type(convierte_edad))
print (convierte_edad < 25)

# La funsion str() nos permite tomar valores numericos y covertilos en cadenas
# 1 Convierte la variable passaword en un string para compararla con la passsaword anterior

passaword = 12345
vieja_passaword = " 54321 "
print (str(passaword) == vieja_passaword)
print (type(passaword))
print (type(vieja_passaword))

# Si usamos int() en un valor de float eliminas los punto decimales y los valores posteriores

price = 9.99
print (int(price))

# Podemos usar float() en un numero entero. Esto agregara un punto decimal y la capacidad de almacenar valores fraccionados

weeks = 10
print (float(weeks))

# Si usamos int() en un valor booleano, el valor numerico equivalente sera 1 para True y 0 para False

member = True
not_member = False

value = int(member)
second_value = int(not_member)

print (value)
print (second_value)

# Podemos usar bool() para convertir una variableen booleana. Si la variable tiene contenido, se convertira en True.
# si eta vacio es 0. Se convierte en False
 
# 1 Convierte estas variables en booleanas y verifique el resultado

miembro = " sam "
middle_name = ""
foot_size = 8.5
siblings = 0

bool_miembro = bool(miembro)
bool_middle_same = bool(middle_name)
bool_foot_size = bool(foot_size)
bool_siblings = bool(siblings)

print ( bool_miembro)
print (bool_middle_same)
print ( bool_foot_size )
print ( bool_siblings )

# Completa elcodigo para mostar los valores booleanos que nos dicen si la persona tiene hijoso mascota

mascota = 2
kids = 0

tiene_mascota = bool(mascota)
tiene_kids = bool(kids)

print ( tiene_mascota)
print ( tiene_kids)
