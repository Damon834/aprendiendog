def calculos_circuito():
    # Seleccionar tipo de circuito
    tipo = input("¿El circuito es serie o paralelo? (s/p): ").lower()
    
    # Validar entrada
    while tipo not in ['s', 'p']:
        print("Opción no válida. Intente nuevamente.")
        tipo = input("¿Serie o paralelo? (s/p): ").lower()

    # Pedir datos
    num_resistencias = int(input("Número de resistencias: "))
    resistencias = []
    
    for i in range(num_resistencias):
        r = float(input(f"Valor de R{i+1} (Ω): "))
        resistencias.append(r)
    
    voltaje = float(input("Voltaje de la fuente (V): "))

    # Cálculos
    if tipo == 's':
        # Circuito en serie
        resistencia_total = sum(resistencias)
        corriente_total = voltaje / resistencia_total
        caidas_voltaje = [corriente_total * r for r in resistencias]
    else:
        # Circuito en paralelo
        inverso_total = sum([1/r for r in resistencias])
        resistencia_total = 1 / inverso_total
        corriente_total = voltaje / resistencia_total
        corrientes_individuales = [voltaje / r for r in resistencias]

    # Mostrar resultados
    print("\n--- Resultados ---")
    print(f"Resistencia total: {resistencia_total:.2f} Ω")
    print(f"Corriente total: {corriente_total:.4f} A")
    
    if tipo == 's':
        print("\nCaídas de voltaje:")
        for i, (r, v) in enumerate(zip(resistencias, caidas_voltaje)):
            print(f"R{i+1} ({r} Ω): {v:.2f} V")
    else:
        print("\nCorrientes individuales:")
        for i, (r, i_r) in enumerate(zip(resistencias, corrientes_individuales)):
            print(f"R{i+1} ({r} Ω): {i_r:.4f} A")

# Ejecutar el programa
calculos_circuito()