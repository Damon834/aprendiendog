# Sabemos como ejecuatar u omitir codigo segun una condicion como age > 16
# El operador and nos permite ejecutar codigo solo si ambas condicioned age>16 y has_permit son True

age = 17
has_permit = True
if age > 16 and has_permit:
    print ("Can drive")

# Codigo and para mostar valid entry solo cuando year es mayor que 1900 y menor que 2020

year = 1998

if year > 1900 and year < 2020:
    print ("valid entry")

# Agregue subway_defect, luego is_sunny y luego distance <= 2 como condiciones para declaracion if

subway_defect = True
is_sunny = True
distance = 2

if subway_defect and is_sunny and distance <= 2:
    print ("Walk to work")

# Para ejecutar codigo cuando cualquiera de las condiciones es True, usamos el operador or

average_grade = "A"
final_score = 1400

if average_grade == "A" or final_score >= 1300:
    print ("Certificate achieved!")

# Podemos usar or para agregar tantas condiciones como queramos como tambien agregar ganno_competencia 

nota_media = "B"
Resultado_Final = 1400
gano_competencia = True

if nota_media == "B" or Resultado_Final >= 1500 or gano_competencia:
    print ("Certificado obtenido") 

# Asigne un valor a nivel para ejecutar el codigo 

puntuacion_mas_alta = 100
puntuacion = 70
nivel = 5
 
if puntuacion > puntuacion_mas_alta or nivel == 5:
    print ("Tu ganaste")