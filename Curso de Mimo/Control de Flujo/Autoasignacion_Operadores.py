# La autoasignacion es cuando configuramos una variable con su propio valo

wallet = 3
wallet = wallet
print (wallet)

# Como podemos autoasignar variables podemos aumentar o disminuir las variables configuradas en numeros 

wallet = 3
wallet = wallet + 1
print (wallet)

# Las variables de autosignacion nos permite rastrear datos que cambian con el tiempo. Por ejemplo un usuario puede agregar 2$ a una billetera y luego eliminar 1$

wallet = 3
wallet = wallet + 2
wallet = wallet - 1
print (wallet)

# Las variables configuradas como cadenas funcionan de la misma manera 

name = "Account name: "
name = name + " Elton"
name = name + " John"
print (name)

# En lugar de reescribir el nombre de la variable podemos usar el operador += para agregar un numero con salse += 1
# Para restar del valor de una variable, usamos el operador -=

sales = 5
sales += 1
print (sales)

sales = 5
sales -= 1
print (sales)