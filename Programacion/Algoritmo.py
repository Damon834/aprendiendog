def calcular_promedio_y_porcentaje():
    """
    Algoritmo que calcula el promedio de 5 alumnos y saca el 20% de ese promedio.
    Validación: notas entre 0.1 y 20
    """
    print("=== CALCULADORA DE PROMEDIO Y 20% ===")
    print("Ingrese las notas de 5 alumnos (entre 0.1 y 20)")
    print("-" * 40)
    
    notas = []
    
    # Recopilar las notas de los 5 alumnos
    for i in range(1, 6):
        while True:
            try:
                nota = float(input(f"Nota del Alumno {i}: "))
                
                # Validar que la nota esté en el rango permitido
                if nota < 0.1 or nota > 20:
                    print("❌ Error: La nota debe estar entre 0.1 y 20")
                    continue
                
                notas.append(nota)
                break
                
            except ValueError:
                print("❌ Error: Por favor ingrese un número válido")
    
    # Calcular la suma
    suma_notas = sum(notas)
    
    # Calcular el promedio
    promedio = suma_notas / 5
    
    # Calcular el 20% del promedio
    veinte_por_ciento = promedio * 0.20
    
    # Mostrar resultados
    print("\n" + "=" * 50)
    print("RESULTADOS:")
    print("=" * 50)
    
    print(f"📝 Notas ingresadas: {notas}")
    print(f"➕ Suma total: {suma_notas:.2f}")
    print(f"📊 Promedio: {promedio:.2f}")
    print(f"💯 20% del promedio: {veinte_por_ciento:.2f}")
    
    return {
        'notas': notas,
        'suma': suma_notas,
        'promedio': promedio,
        'veinte_porciento': veinte_por_ciento
    }

def validar_nota(nota):
    """
    Función auxiliar para validar una nota individual
    """
    return 0.1 <= nota <= 20

def calcular_con_lista_predefinida(notas_lista):
    """
    Versión del algoritmo que acepta una lista de notas como parámetro
    """
    # Validar que sean exactamente 5 notas
    if len(notas_lista) != 5:
        raise ValueError("Se requieren exactamente 5 notas")
    
    # Validar cada nota
    for i, nota in enumerate(notas_lista):
        if not validar_nota(nota):
            raise ValueError(f"La nota {i+1} ({nota}) debe estar entre 0.1 y 20")
    
    suma = sum(notas_lista)
    promedio = suma / 5
    veinte_por_ciento = promedio * 0.20
    
    return {
        'notas': notas_lista,
        'suma': suma,
        'promedio': promedio,
        'veinte_porciento': veinte_por_ciento
    }

# Ejemplo de uso
if __name__ == "__main__":
    print("🎓 SISTEMA DE CÁLCULO DE NOTAS")
    print("=" * 40)
    
    # Opción 1: Ingreso manual
    print("\n1️⃣ INGRESO MANUAL DE NOTAS:")
    resultado = calcular_promedio_y_porcentaje()
    
    print("\n" + "=" * 50)
    
    # Opción 2: Ejemplo con lista predefinida
    print("2️⃣ EJEMPLO CON NOTAS PREDEFINIDAS:")
    notas_ejemplo = [15.5, 18.2, 12.8, 16.7, 14.3]
    
    try:
        resultado_ejemplo = calcular_con_lista_predefinida(notas_ejemplo)
        print(f"📝 Notas: {resultado_ejemplo['notas']}")
        print(f"➕ Suma: {resultado_ejemplo['suma']:.2f}")
        print(f"📊 Promedio: {resultado_ejemplo['promedio']:.2f}")
        print(f"💯 20% del promedio: {resultado_ejemplo['veinte_porciento']:.2f}")
    except ValueError as e:
        print(f"❌ Error: {e}")