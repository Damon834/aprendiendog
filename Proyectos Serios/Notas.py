# Datos de las materias
materias_seccion1 = [
    {"nombre": "Matemáticas 1", "calificacion": 6.9, "creditos": 5},
    {"nombre": "Dibujo 1", "calificacion": 5.3, "creditos": 2},
    {"nombre": "Inglés 1", "calificacion": 5.1, "creditos": 2},
    {"nombre": "Química", "calificacion": 4.4, "creditos": 3},
    {"nombre": "Lenguaje y comunicación", "calificacion": 7.4, "creditos": 2},
    {"nombre": "Lógica", "calificacion": 8.3, "creditos": 2},
    {"nombre": "Educación física", "calificacion": 7.1, "creditos": 1},
]

materias_seccion2 = [
    {"nombre": "Matemáticas 2", "calificacion": 7.3, "creditos": 5},
    {"nombre": "Física 1", "calificacion": 5.0, "creditos": 4},
    {"nombre": "Deporte", "calificacion": 8.1, "creditos": 1},
    {"nombre": "Laboratorio de física 1", "calificacion": 5.1, "creditos": 1},
]

# Función para calcular el índice académico
def calcular_indice(materias):
    total_productos = sum(m["calificacion"] * m["creditos"] for m in materias)
    total_creditos = sum(m["creditos"] for m in materias)
    return total_productos, total_creditos

# Calcular los totales de cada sección
productos_seccion1, creditos_seccion1 = calcular_indice(materias_seccion1)
productos_seccion2, creditos_seccion2 = calcular_indice(materias_seccion2)

# Calcular el índice académico total
total_productos = productos_seccion1 + productos_seccion2
total_creditos = creditos_seccion1 + creditos_seccion2
indice_total = total_productos / total_creditos

# Mostrar los resultados
print(f"Suma de productos (Sección 1): {productos_seccion1}")
print(f"Suma de créditos (Sección 1): {creditos_seccion1}")
print(f"Suma de productos (Sección 2): {productos_seccion2}")
print(f"Suma de créditos (Sección 2): {creditos_seccion2}")
print(f"Suma total de productos: {total_productos}")
print(f"Suma total de créditos: {total_creditos}")
print(f"Índice académico total: {indice_total:.2f}")
