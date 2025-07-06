import os
import json
from datetime import datetime

class SistemaJugadores:
    def __init__(self):
        self.jugadores = []
        self.archivo_datos = "jugadores.json"
        self.cargar_datos()
    
    def cargar_datos(self):
        """Carga los datos de jugadores desde un archivo JSON"""
        try:
            with open(self.archivo_datos, 'r', encoding='utf-8') as f:
                self.jugadores = json.load(f)
        except FileNotFoundError:
            self.jugadores = []
    
    def guardar_datos(self):
        """Guarda los datos de jugadores en un archivo JSON"""
        with open(self.archivo_datos, 'w', encoding='utf-8') as f:
            json.dump(self.jugadores, f, indent=2, ensure_ascii=False)
    
    def limpiar_pantalla(self):
        """Limpia la pantalla de la consola"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def mostrar_menu(self):
        """Muestra el menú principal"""
        self.limpiar_pantalla()
        print("=" * 50)
        print("           MENU PRINCIPAL")
        print("=" * 50)
        print("--- MENU PRINCIPAL ---")
        print("1. Agregar jugador")
        print("2. Eliminar jugador")
        print("3. Modificar jugador")
        print("4. Consultar jugador individual")
        print("5. Consultar jugadores (general)")
        print("6. Salir")
        print("Seleccione una opción:")
    
    def agregar_jugador(self):
        """Agrega un nuevo jugador al sistema"""
        self.limpiar_pantalla()
        print("=== AGREGAR JUGADOR ===")
        
        try:
            nombre = input("Nombre completo: ").strip()
            if not nombre:
                print("El nombre no puede estar vacío.")
                input("Presione Enter para continuar...")
                return
            
            cedula = input("Cédula: ").strip()
            if not cedula:
                print("La cédula no puede estar vacía.")
                input("Presione Enter para continuar...")
                return
            
            # Verificar si ya existe un jugador con esa cédula
            for jugador in self.jugadores:
                if jugador['cedula'] == cedula:
                    print("Ya existe un jugador con esa cédula.")
                    input("Presione Enter para continuar...")
                    return
            
            edad = int(input("Edad: "))
            posicion = input("Posición: ").strip()
            equipo = input("Equipo: ").strip()
            
            nuevo_jugador = {
                'nombre': nombre,
                'cedula': cedula,
                'edad': edad,
                'posicion': posicion,
                'equipo': equipo,
                'fecha_registro': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            
            self.jugadores.append(nuevo_jugador)
            self.guardar_datos()
            
            print(f"\nJugador {nombre} agregado exitosamente!")
            
        except ValueError:
            print("Error: La edad debe ser un número válido.")
        except Exception as e:
            print(f"Error al agregar jugador: {e}")
        
        input("Presione Enter para continuar...")
    
    def eliminar_jugador(self):
        """Elimina un jugador del sistema"""
        self.limpiar_pantalla()
        print("=== ELIMINAR JUGADOR ===")
        
        if not self.jugadores:
            print("No hay jugadores registrados.")
            input("Presione Enter para continuar...")
            return
        
        cedula = input("Ingrese la cédula del jugador a eliminar: ").strip()
        
        for i, jugador in enumerate(self.jugadores):
            if jugador['cedula'] == cedula:
                print(f"\nJugador encontrado:")
                print(f"Nombre: {jugador['nombre']}")
                print(f"Cédula: {jugador['cedula']}")
                print(f"Equipo: {jugador['equipo']}")
                
                confirmacion = input("\n¿Está seguro de eliminar este jugador? (s/n): ").lower()
                if confirmacion == 's':
                    self.jugadores.pop(i)
                    self.guardar_datos()
                    print("Jugador eliminado exitosamente!")
                else:
                    print("Eliminación cancelada.")
                
                input("Presione Enter para continuar...")
                return
        
        print("No se encontró ningún jugador con esa cédula.")
        input("Presione Enter para continuar...")
    
    def modificar_jugador(self):
        """Modifica los datos de un jugador existente"""
        self.limpiar_pantalla()
        print("=== MODIFICAR JUGADOR ===")
        
        if not self.jugadores:
            print("No hay jugadores registrados.")
            input("Presione Enter para continuar...")
            return
        
        cedula = input("Ingrese la cédula del jugador a modificar: ").strip()
        
        for jugador in self.jugadores:
            if jugador['cedula'] == cedula:
                print(f"\nJugador encontrado:")
                print(f"1. Nombre: {jugador['nombre']}")
                print(f"2. Edad: {jugador['edad']}")
                print(f"3. Posición: {jugador['posicion']}")
                print(f"4. Equipo: {jugador['equipo']}")
                
                try:
                    opcion = int(input("\n¿Qué campo desea modificar? (1-4): "))
                    
                    if opcion == 1:
                        nuevo_nombre = input("Nuevo nombre: ").strip()
                        if nuevo_nombre:
                            jugador['nombre'] = nuevo_nombre
                    elif opcion == 2:
                        nueva_edad = int(input("Nueva edad: "))
                        jugador['edad'] = nueva_edad
                    elif opcion == 3:
                        nueva_posicion = input("Nueva posición: ").strip()
                        if nueva_posicion:
                            jugador['posicion'] = nueva_posicion
                    elif opcion == 4:
                        nuevo_equipo = input("Nuevo equipo: ").strip()
                        if nuevo_equipo:
                            jugador['equipo'] = nuevo_equipo
                    else:
                        print("Opción no válida.")
                        input("Presione Enter para continuar...")
                        return
                    
                    self.guardar_datos()
                    print("Jugador modificado exitosamente!")
                    
                except ValueError:
                    print("Error: Entrada no válida.")
                
                input("Presione Enter para continuar...")
                return
        
        print("No se encontró ningún jugador con esa cédula.")
        input("Presione Enter para continuar...")
    
    def consultar_jugador_individual(self):
        """Consulta los datos de un jugador específico"""
        self.limpiar_pantalla()
        print("=== CONSULTAR JUGADOR INDIVIDUAL ===")
        
        if not self.jugadores:
            print("No hay jugadores registrados.")
            input("Presione Enter para continuar...")
            return
        
        cedula = input("Ingrese la cédula del jugador: ").strip()
        
        for jugador in self.jugadores:
            if jugador['cedula'] == cedula:
                print(f"\n--- INFORMACIÓN DEL JUGADOR ---")
                print(f"Nombre: {jugador['nombre']}")
                print(f"Cédula: {jugador['cedula']}")
                print(f"Edad: {jugador['edad']} años")
                print(f"Posición: {jugador['posicion']}")
                print(f"Equipo: {jugador['equipo']}")
                print(f"Fecha de registro: {jugador['fecha_registro']}")
                
                input("\nPresione Enter para continuar...")
                return
        
        print("No se encontró ningún jugador con esa cédula.")
        input("Presione Enter para continuar...")
    
    def consultar_jugadores_general(self):
        """Muestra todos los jugadores registrados"""
        self.limpiar_pantalla()
        print("=== CONSULTAR JUGADORES (GENERAL) ===")
        
        if not self.jugadores:
            print("No hay jugadores registrados.")
            input("Presione Enter para continuar...")
            return
        
        print(f"\nTotal de jugadores registrados: {len(self.jugadores)}")
        print("-" * 80)
        
        for i, jugador in enumerate(self.jugadores, 1):
            print(f"{i}. {jugador['nombre']} - {jugador['cedula']}")
            print(f"   Edad: {jugador['edad']} | Posición: {jugador['posicion']} | Equipo: {jugador['equipo']}")
            print("-" * 80)
        
        input("\nPresione Enter para continuar...")
    
    def ejecutar(self):
        """Ejecuta el sistema principal"""
        while True:
            self.mostrar_menu()
            
            try:
                opcion = input().strip()
                
                if opcion == '1':
                    self.agregar_jugador()
                elif opcion == '2':
                    self.eliminar_jugador()
                elif opcion == '3':
                    self.modificar_jugador()
                elif opcion == '4':
                    self.consultar_jugador_individual()
                elif opcion == '5':
                    self.consultar_jugadores_general()
                elif opcion == '6':
                    print("¡Gracias por usar el sistema!")
                    break
                else:
                    print("Opción no válida. Intente nuevamente.")
                    input("Presione Enter para continuar...")
                    
            except KeyboardInterrupt:
                print("\n\nSaliendo del sistema...")
                break
            except Exception as e:
                print(f"Error inesperado: {e}")
                input("Presione Enter para continuar...")

# Ejecutar el sistema
if __name__ == "__main__":
    sistema = SistemaJugadores()
    sistema.ejecutar()