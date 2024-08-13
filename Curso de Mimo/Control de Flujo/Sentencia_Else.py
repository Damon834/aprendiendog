# Agreguemos otra declaracion if que use el operador not para ejecutar un bloque de codigo diferente si la condicion es False

avilabre = True

if avilabre:
    print ("In stock")

if not avilabre:
    print ("Out of stock")

# En lugar de crear dos declaraciones if usamos una declaracion if/else para lograr el mismo  resultado 
# La declaracion else de una declaracion if/else siempre va al final 

disponible = False

if disponible:
    print ("1 en stock")

else:
    print ("1 agotado")

 
# La declaracion else no necesita su propia condicion. Esto se debe a que manejar los casos en los que la condicion if es False

number = 99

if number == 1:
    print ("It's 1")

else:
    print ("It' not 1")

# Establezca ppints en 7600 para ejecute el bloque de codigo de la instruccion else 

points = 7600
points_needed = 8000

if points >= points_needed:
    print ("You're level 2!")

else:
    left = points_needed - points
    print ("Points till level 2:!")
    print (left)
