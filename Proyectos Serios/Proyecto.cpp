#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <cstdlib>
#include <limits>
#include <ctime>

using namespace std;

struct Jugador
{
    string nombre;
    string cedula;
    int edad;
    string posicion;
    string equipo;
    string fecha_registro;
};

class SistemaJugadores
{
private:
    vector<Jugador> jugadores;
    string archivo_datos;

public:
    SistemaJugadores() : archivo_datos("jugadores.txt")
    {
        cargar_datos();
    }

    void limpiar_pantalla()
    {
#ifdef _WIN32
        system("cls");
#else
        system("clear");
#endif
    }

    void pausar()
    {
        cout << "\nPresione Enter para continuar...";
        cin.ignore();
        cin.get();
    }

    string obtener_fecha_actual()
    {
        time_t now = time(0);
        char *dt = ctime(&now);
        string fecha = dt;
        fecha.pop_back(); // Eliminar el salto de línea
        return fecha;
    }

    void cargar_datos()
    {
        ifstream archivo(archivo_datos);
        if (!archivo.is_open())
        {
            return; // Si no existe el archivo, comenzar con lista vacía
        }

        string linea;
        while (getline(archivo, linea))
        {
            if (linea.empty())
                continue;

            Jugador jugador;
            stringstream ss(linea);
            string campo;

            getline(ss, jugador.nombre, '|');
            getline(ss, jugador.cedula, '|');
            getline(ss, campo, '|');
            jugador.edad = stoi(campo);
            getline(ss, jugador.posicion, '|');
            getline(ss, jugador.equipo, '|');
            getline(ss, jugador.fecha_registro, '|');

            jugadores.push_back(jugador);
        }
        archivo.close();
    }

    void guardar_datos()
    {
        ofstream archivo(archivo_datos);
        if (!archivo.is_open())
        {
            cout << "Error al abrir el archivo para guardar." << endl;
            return;
        }

        for (const auto &jugador : jugadores)
        {
            archivo << jugador.nombre << "|"
                    << jugador.cedula << "|"
                    << jugador.edad << "|"
                    << jugador.posicion << "|"
                    << jugador.equipo << "|"
                    << jugador.fecha_registro << endl;
        }
        archivo.close();
    }

    void mostrar_menu()
    {
        limpiar_pantalla();
        cout << "==================================================" << endl;
        cout << "           MENU PRINCIPAL" << endl;
        cout << "==================================================" << endl;
        cout << "--- MENU PRINCIPAL ---" << endl;
        cout << "1. Agregar jugador" << endl;
        cout << "2. Eliminar jugador" << endl;
        cout << "3. Modificar jugador" << endl;
        cout << "4. Consultar jugador individual" << endl;
        cout << "5. Consultar jugadores (general)" << endl;
        cout << "6. Salir" << endl;
        cout << "Seleccione una opción: ";
    }

    bool cedula_existe(const string &cedula)
    {
        for (const auto &jugador : jugadores)
        {
            if (jugador.cedula == cedula)
            {
                return true;
            }
        }
        return false;
    }

    void agregar_jugador()
    {
        limpiar_pantalla();
        cout << "=== AGREGAR JUGADOR ===" << endl;

        Jugador nuevo_jugador;

        cout << "Nombre completo: ";
        cin.ignore();
        getline(cin, nuevo_jugador.nombre);

        if (nuevo_jugador.nombre.empty())
        {
            cout << "El nombre no puede estar vacío." << endl;
            pausar();
            return;
        }

        cout << "Cédula: ";
        getline(cin, nuevo_jugador.cedula);

        if (nuevo_jugador.cedula.empty())
        {
            cout << "La cédula no puede estar vacía." << endl;
            pausar();
            return;
        }

        if (cedula_existe(nuevo_jugador.cedula))
        {
            cout << "Ya existe un jugador con esa cédula." << endl;
            pausar();
            return;
        }

        cout << "Edad: ";
        while (!(cin >> nuevo_jugador.edad) || nuevo_jugador.edad < 0)
        {
            cout << "Error: Ingrese una edad válida: ";
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
        }

        cout << "Posición: ";
        cin.ignore();
        getline(cin, nuevo_jugador.posicion);

        cout << "Equipo: ";
        getline(cin, nuevo_jugador.equipo);

        nuevo_jugador.fecha_registro = obtener_fecha_actual();

        jugadores.push_back(nuevo_jugador);
        guardar_datos();

        cout << "\nJugador " << nuevo_jugador.nombre << " agregado exitosamente!" << endl;
        pausar();
    }

    void eliminar_jugador()
    {
        limpiar_pantalla();
        cout << "=== ELIMINAR JUGADOR ===" << endl;

        if (jugadores.empty())
        {
            cout << "No hay jugadores registrados." << endl;
            pausar();
            return;
        }

        string cedula;
        cout << "Ingrese la cédula del jugador a eliminar: ";
        cin.ignore();
        getline(cin, cedula);

        for (auto it = jugadores.begin(); it != jugadores.end(); ++it)
        {
            if (it->cedula == cedula)
            {
                cout << "\nJugador encontrado:" << endl;
                cout << "Nombre: " << it->nombre << endl;
                cout << "Cédula: " << it->cedula << endl;
                cout << "Equipo: " << it->equipo << endl;

                char confirmacion;
                cout << "\n¿Está seguro de eliminar este jugador? (s/n): ";
                cin >> confirmacion;

                if (confirmacion == 's' || confirmacion == 'S')
                {
                    jugadores.erase(it);
                    guardar_datos();
                    cout << "Jugador eliminado exitosamente!" << endl;
                }
                else
                {
                    cout << "Eliminación cancelada." << endl;
                }

                pausar();
                return;
            }
        }

        cout << "No se encontró ningún jugador con esa cédula." << endl;
        pausar();
    }

    void modificar_jugador()
    {
        limpiar_pantalla();
        cout << "=== MODIFICAR JUGADOR ===" << endl;

        if (jugadores.empty())
        {
            cout << "No hay jugadores registrados." << endl;
            pausar();
            return;
        }

        string cedula;
        cout << "Ingrese la cédula del jugador a modificar: ";
        cin.ignore();
        getline(cin, cedula);

        for (auto &jugador : jugadores)
        {
            if (jugador.cedula == cedula)
            {
                cout << "\nJugador encontrado:" << endl;
                cout << "1. Nombre: " << jugador.nombre << endl;
                cout << "2. Edad: " << jugador.edad << endl;
                cout << "3. Posición: " << jugador.posicion << endl;
                cout << "4. Equipo: " << jugador.equipo << endl;

                int opcion;
                cout << "\n¿Qué campo desea modificar? (1-4): ";

                while (!(cin >> opcion) || opcion < 1 || opcion > 4)
                {
                    cout << "Error: Ingrese una opción válida (1-4): ";
                    cin.clear();
                    cin.ignore(numeric_limits<streamsize>::max(), '\n');
                }

                cin.ignore();

                switch (opcion)
                {
                case 1:
                {
                    string nuevo_nombre;
                    cout << "Nuevo nombre: ";
                    getline(cin, nuevo_nombre);
                    if (!nuevo_nombre.empty())
                    {
                        jugador.nombre = nuevo_nombre;
                    }
                    break;
                }
                case 2:
                {
                    int nueva_edad;
                    cout << "Nueva edad: ";
                    while (!(cin >> nueva_edad) || nueva_edad < 0)
                    {
                        cout << "Error: Ingrese una edad válida: ";
                        cin.clear();
                        cin.ignore(numeric_limits<streamsize>::max(), '\n');
                    }
                    jugador.edad = nueva_edad;
                    break;
                }
                case 3:
                {
                    string nueva_posicion;
                    cout << "Nueva posición: ";
                    getline(cin, nueva_posicion);
                    if (!nueva_posicion.empty())
                    {
                        jugador.posicion = nueva_posicion;
                    }
                    break;
                }
                case 4:
                {
                    string nuevo_equipo;
                    cout << "Nuevo equipo: ";
                    getline(cin, nuevo_equipo);
                    if (!nuevo_equipo.empty())
                    {
                        jugador.equipo = nuevo_equipo;
                    }
                    break;
                }
                }

                guardar_datos();
                cout << "Jugador modificado exitosamente!" << endl;
                pausar();
                return;
            }
        }

        cout << "No se encontró ningún jugador con esa cédula." << endl;
        pausar();
    }

    void consultar_jugador_individual()
    {
        limpiar_pantalla();
        cout << "=== CONSULTAR JUGADOR INDIVIDUAL ===" << endl;

        if (jugadores.empty())
        {
            cout << "No hay jugadores registrados." << endl;
            pausar();
            return;
        }

        string cedula;
        cout << "Ingrese la cédula del jugador: ";
        cin.ignore();
        getline(cin, cedula);

        for (const auto &jugador : jugadores)
        {
            if (jugador.cedula == cedula)
            {
                cout << "\n--- INFORMACIÓN DEL JUGADOR ---" << endl;
                cout << "Nombre: " << jugador.nombre << endl;
                cout << "Cédula: " << jugador.cedula << endl;
                cout << "Edad: " << jugador.edad << " años" << endl;
                cout << "Posición: " << jugador.posicion << endl;
                cout << "Equipo: " << jugador.equipo << endl;
                cout << "Fecha de registro: " << jugador.fecha_registro << endl;

                pausar();
                return;
            }
        }

        cout << "No se encontró ningún jugador con esa cédula." << endl;
        pausar();
    }

    void consultar_jugadores_general()
    {
        limpiar_pantalla();
        cout << "=== CONSULTAR JUGADORES (GENERAL) ===" << endl;

        if (jugadores.empty())
        {
            cout << "No hay jugadores registrados." << endl;
            pausar();
            return;
        }

        cout << "\nTotal de jugadores registrados: " << jugadores.size() << endl;
        cout << string(80, '-') << endl;

        for (size_t i = 0; i < jugadores.size(); ++i)
        {
            cout << (i + 1) << ". " << jugadores[i].nombre << " - " << jugadores[i].cedula << endl;
            cout << "   Edad: " << jugadores[i].edad
                 << " | Posición: " << jugadores[i].posicion
                 << " | Equipo: " << jugadores[i].equipo << endl;
            cout << string(80, '-') << endl;
        }

        pausar();
    }

    void ejecutar()
    {
        int opcion;

        while (true)
        {
            mostrar_menu();

            while (!(cin >> opcion) || opcion < 1 || opcion > 6)
            {
                cout << "Error: Ingrese una opción válida (1-6): ";
                cin.clear();
                cin.ignore(numeric_limits<streamsize>::max(), '\n');
            }

            switch (opcion)
            {
            case 1:
                agregar_jugador();
                break;
            case 2:
                eliminar_jugador();
                break;
            case 3:
                modificar_jugador();
                break;
            case 4:
                consultar_jugador_individual();
                break;
            case 5:
                consultar_jugadores_general();
                break;
            case 6:
                cout << "¡Gracias por usar el sistema!" << endl;
                return;
            default:
                cout << "Opción no válida. Intente nuevamente." << endl;
                pausar();
            }
        }
    }
};

int main()
{
    SistemaJugadores sistema;
    sistema.ejecutar();
    return 0;
}