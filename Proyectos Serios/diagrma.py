import matplotlib.pyplot as plt

import matplotlib.pyplot as plt
import numpy as np

# Configuración del gráfico
plt.figure(figsize=(10, 6))
plt.title("Diagrama de Fases del SO₂")
plt.xlabel("Temperatura (°C)")
plt.ylabel("Presión (atm)")
plt.grid(True, linestyle='--', alpha=0.7)

# Datos clave
punto_triple = (-75.5, 0.00165)
punto_critico = (157, 78)
punto_ebullicion = (-10, 1)
punto_congelacion = (-72.7, 1)

# Líneas de equilibrio
# Sólido-Líquido (desde punto triple hasta punto de congelación)
x_sol_liq = [punto_triple[0], punto_congelacion[0]]
y_sol_liq = [punto_triple[1], punto_congelacion[1]]

# Líquido-Gas (desde punto triple hasta punto crítico, pasando por ebullición)
x_liq_gas = [punto_triple[0], punto_ebullicion[0], punto_critico[0]]
y_liq_gas = [punto_triple[1], punto_ebullicion[1], punto_critico[1]]

# Sólido-Gas (extrapolación desde punto triple hacia T menores)
x_sol_gas = [punto_triple[0], -85]  # Extensión arbitraria
y_sol_gas = [punto_triple[1], 0.0005]

# Procesos
# a) Isobárico desde punto triple (rojo)
x_proceso_a = [punto_triple[0], 0]
y_proceso_a = [punto_triple[1], punto_triple[1]]

# b) Isobárico desde punto crítico (azul)
x_proceso_b = [punto_critico[0], punto_critico[0]]
y_proceso_b = [punto_critico[1], 1]

# c) Isotérmico + Isobárico (verde)
x_proceso_c1 = [punto_triple[0], punto_triple[0]]
y_proceso_c1 = [punto_triple[1], 78]
x_proceso_c2 = [punto_triple[0], 157]
y_proceso_c2 = [78, 78]

# Dibujar líneas
plt.plot(x_sol_liq, y_sol_liq, 'k-', label='Sólido-Líquido')
plt.plot(x_liq_gas, y_liq_gas, 'k-', label='Líquido-Gas')
plt.plot(x_sol_gas, y_sol_gas, 'k-', label='Sólido-Gas')
plt.plot(x_proceso_a, y_proceso_a, 'r--', label='Proceso a)')
plt.plot(x_proceso_b, y_proceso_b, 'b--', label='Proceso b)')
plt.plot(x_proceso_c1, y_proceso_c1, 'g--')
plt.plot(x_proceso_c2, y_proceso_c2, 'g--', label='Proceso c)')

# Marcar puntos clave
plt.scatter(*punto_triple, color='black', zorder=5, label='Punto Triple')
plt.scatter(*punto_critico, color='red', zorder=5, label='Punto Crítico')

# Etiquetas y leyenda
plt.yscale('log')  # Escala logarítmica para presión
plt.legend()
plt.annotate('Sólido', xy=(-80, 0.1), fontsize=12)
plt.annotate('Líquido', xy=(-50, 10), fontsize=12)
plt.annotate('Gas', xy=(50, 0.01), fontsize=12)
plt.annotate('Fluido Supercrítico', xy=(100, 100), fontsize=12)

# Guardar y mostrar
plt.savefig('diagrama_fases_SO2.png', dpi=300)
plt.show()



