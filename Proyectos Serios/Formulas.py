import sympy as sp
import matplotlib.pyplot as plt

# Configuración para mostrar fórmulas
plt.rcParams['text.usetex'] = False  # Desactivar si no tienes LaTeX

def resolver_limite():
    # Definir símbolos
    x, y, u = sp.symbols('x y u')
    
    # Expresión original
    expr = (sp.sqrt(x*y - 1) + x**3*y**3 - 1)/(sp.sqrt(x**2*y**2 - 1))
    
    # Sustitución u = xy - 1
    expr_sub = expr.subs(x*y, u + 1).subs(x**2*y**2, (u + 1)**2)
    expr_simplificado = sp.simplify(expr_sub)
    
    # Calcular límite cuando u → 0
    limite = sp.limit(expr_simplificado, u, 0)
    
    # Crear imagen con el proceso
    fig = plt.figure(figsize=(12, 8))
    plt.axis('off')
    
    texto = [
        r"Problema: $\lim_{(x,y) \to (1,1)} \frac{\sqrt{xy-1} + x^3y^3 - 1}{\sqrt{x^2y^2-1}}$",
        "",
        "Paso 1: Sustitución $u = xy - 1$",
        r"$\Rightarrow xy = u + 1$",
        r"$\Rightarrow x^2y^2 = (u + 1)^2$",
        "",
        "Expresión transformada:",
        r"$\frac{\sqrt{u} + (u + 1)^3 - 1}{\sqrt{(u + 1)^2 - 1}}$",
        "",
        "Paso 2: Simplificar el numerador y denominador",
        r"Numerador: $\sqrt{u} + u^3 + 3u^2 + 3u$",
        r"Denominador: $\sqrt{u(u + 2)}$",
        "",
        "Paso 3: Factor común $\sqrt{u}$",
        r"$\frac{\sqrt{u}(1 + 3\sqrt{u} + 3u^{3/2} + u^{5/2})}{\sqrt{u}\sqrt{u + 2}}$",
        "",
        "Paso 4: Cancelar $\sqrt{u}$ y evaluar límite cuando $u \to 0$",
        r"$\lim_{u \to 0} \frac{1 + 3\sqrt{u} + 3u^{3/2} + u^{5/2}}{\sqrt{u + 2}} = \frac{1}{\sqrt{2}}$",
        "",
        f"Resultado final: $\boxed{{\\frac{{1}}{{\\sqrt{{2}}}} \\approx {1/sp.sqrt(2):.4f}$"
    ]
    
    plt.text(0.1, 0.95, "\n".join(texto), ha='left', va='top', fontsize=14)
    plt.title("Resolución del Límite Multivariable", fontsize=16)
    plt.tight_layout()
    plt.savefig('limite_resuelto.png')
    plt.show()

    return limite

# Ejecutar la resolución
resultado = resolver_limite()
print(f"El valor del límite es: {resultado}")