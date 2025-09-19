import tkinter as tk
from tkinter import messagebox
import numpy as np

class EquationSolverApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Sistemas de Ecuaciones")
        self.root.geometry("650x400") # Tamaño inicial de la ventana

        # --- Variables ---
        self.num_vars = tk.IntVar(value=2)
        self.entry_widgets = []
        self.b_entry_widgets = []

        # --- Configuración del Frame Principal ---
        main_frame = tk.Frame(root, padx=10, pady=10)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # --- Frame de Selección ---
        top_frame = tk.Frame(main_frame)
        top_frame.pack(pady=5, fill=tk.X)

        tk.Label(top_frame, text="Número de incógnitas:", font=("Arial", 12)).pack(side=tk.LEFT, padx=5)
        options = [2, 3, 4, 5, 6]
        self.vars_menu = tk.OptionMenu(top_frame, self.num_vars, *options, command=self.create_input_grid)
        self.vars_menu.config(font=("Arial", 11), width=5)
        self.vars_menu.pack(side=tk.LEFT)

        # --- Frame para la Matriz de Ecuaciones ---
        self.grid_frame = tk.Frame(main_frame)
        self.grid_frame.pack(pady=10, expand=True)

        # --- Frame de Botones y Resultados ---
        bottom_frame = tk.Frame(main_frame)
        bottom_frame.pack(pady=10, fill=tk.X)
        
        self.solve_button = tk.Button(bottom_frame, text="Resolver", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", command=self.solve_equations)
        self.solve_button.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.X)

        self.clear_button = tk.Button(bottom_frame, text="Limpiar", font=("Arial", 12), bg="#f44336", fg="white", command=self.clear_fields)
        self.clear_button.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.X)

        self.result_label = tk.Label(main_frame, text="La solución aparecerá aquí", font=("Arial", 12, "italic"), wraplength=500)
        self.result_label.pack(pady=10)

        # Crear la primera parrilla de entrada
        self.create_input_grid()

    def create_input_grid(self, *args):
        # Limpiar widgets anteriores
        for widget in self.grid_frame.winfo_children():
            widget.destroy()

        self.entry_widgets = []
        self.b_entry_widgets = []
        n = self.num_vars.get()

        for i in range(n):
            row_entries = []
            for j in range(n):
                # Coeficiente de la matriz A
                entry = tk.Entry(self.grid_frame, width=5, font=("Arial", 11), justify='center')
                entry.grid(row=i, column=j*2, padx=5, pady=5)
                row_entries.append(entry)

                # Etiqueta de la variable (x1, x2, ...)
                if j < n - 1:
                    tk.Label(self.grid_frame, text=f"x{j+1} +", font=("Arial", 11)).grid(row=i, column=j*2 + 1)
                else:
                    tk.Label(self.grid_frame, text=f"x{j+1}", font=("Arial", 11)).grid(row=i, column=j*2 + 1)

            # Símbolo de igual
            tk.Label(self.grid_frame, text="=", font=("Arial", 11, "bold")).grid(row=i, column=n*2, padx=5)
            
            # Coeficiente del vector b
            b_entry = tk.Entry(self.grid_frame, width=5, font=("Arial", 11), justify='center')
            b_entry.grid(row=i, column=n*2 + 1, padx=5, pady=5)
            self.b_entry_widgets.append(b_entry)
            self.entry_widgets.append(row_entries)

    def solve_equations(self):
        n = self.num_vars.get()
        
        try:
            # Construir la matriz A y el vector b a partir de los valores de entrada
            A = np.array([[float(entry.get()) for entry in row] for row in self.entry_widgets])
            b = np.array([float(entry.get()) for entry in self.b_entry_widgets])
            
            # Resolver el sistema usando NumPy
            solution = np.linalg.solve(A, b)
            
            # Formatear y mostrar la solución
            result_str = "Solución:\n"
            result_str += ", ".join([f"x{i+1} = {val:.4f}" for i, val in enumerate(solution)])
            self.result_label.config(text=result_str, fg="green", font=("Arial", 12, "bold"))

        except ValueError:
            # Error si un campo está vacío o no es un número
            self.result_label.config(text="Error: Todos los campos deben contener números.", fg="red", font=("Arial", 12, "italic"))
            messagebox.showerror("Error de Entrada", "Por favor, asegúrate de que todos los campos estén llenos con valores numéricos.")
        except np.linalg.LinAlgError:
            # Error si el sistema no tiene solución única
            self.result_label.config(text="Error: El sistema no tiene una solución única (matriz singular).", fg="red", font=("Arial", 12, "italic"))
            messagebox.showwarning("Error de Cálculo", "No se pudo resolver el sistema. La matriz de coeficientes es singular.")
        except Exception as e:
            # Capturar otros posibles errores
            self.result_label.config(text=f"Ocurrió un error inesperado: {e}", fg="red", font=("Arial", 12, "italic"))
            messagebox.showerror("Error Inesperado", f"Ha ocurrido un error:\n{e}")

    def clear_fields(self):
        # Limpiar todos los campos de entrada
        for row in self.entry_widgets:
            for entry in row:
                entry.delete(0, tk.END)
        for entry in self.b_entry_widgets:
            entry.delete(0, tk.END)
        
        # Restablecer la etiqueta de resultado
        self.result_label.config(text="La solución aparecerá aquí", fg="black", font=("Arial", 12, "italic"))


if __name__ == "__main__":
    root = tk.Tk()
    app = EquationSolverApp(root)
    root.mainloop()