import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


# ==========================================================
# CAMPO DE PENDIENTES
# ==========================================================

def campo_pendientes(funcion, xmin, xmax, ymin, ymax, n=20, largo=0.035):
    """Dibuja el campo de pendientes con flechas de largo visual constante
    y con el ángulo correcto aunque los ejes tengan escalas distintas."""

    x = np.linspace(xmin, xmax, n)
    y = np.linspace(ymin, ymax, n)
    X, Y = np.meshgrid(x, y)

    with np.errstate(over="ignore", invalid="ignore"):
        M = funcion(X, Y)

    M = np.clip(np.nan_to_num(M, nan=0.0, posinf=1e6, neginf=-1e6), -1e6, 1e6)

    dx = xmax - xmin
    dy = ymax - ymin

    # Normaliza en coordenadas de pantalla, no en coordenadas de datos
    norma = np.sqrt((1.0 / dx) ** 2 + (M / dy) ** 2)
    escala = largo / norma

    U = escala
    V = escala * M

    plt.quiver(X, Y, U, V,
               angles="xy", scale_units="xy", scale=1,
               width=0.0025, color="0.4")


# ==========================================================
# ECUACIONES DIFERENCIALES
# ==========================================================

def f_a(x, y):
    return -y - np.sin(x)


def f_b(x, y):
    return x + y


def f_c(x, y):
    return -x**2 + np.sin(y)


def f_d(x, y):
    return (6*x - 3*x*y) / (x**2 + 1)


def f_e(x, y):
    return x * np.exp(y)


def f_f(x, y):
    return x - y


# ==========================================================
# RESOLVER PASANDO POR (x0, y0): hacia atrás y hacia adelante
# ==========================================================

def resolver(funcion, x0, y0, xmin, xmax, ymin=None, ymax=None):

    tramos = []

    for destino in (xmin, xmax):

        if np.isclose(destino, x0):
            continue

        malla = np.linspace(x0, destino, 400)

        sol = solve_ivp(funcion, [x0, destino], [y0],
                        t_eval=malla, rtol=1e-8, atol=1e-10)

        tramos.append((sol.t, sol.y[0]))

    # tramo izquierdo invertido + tramo derecho
    t = np.concatenate([tramos[0][0][::-1], tramos[1][0]])
    v = np.concatenate([tramos[0][1][::-1], tramos[1][1]])

    return t, v


# ==========================================================
# GRÁFICAS
# ==========================================================

def graficar_campo(funcion, titulo, xmin, xmax, ymin, ymax):

    plt.figure(figsize=(8, 6))
    campo_pendientes(funcion, xmin, xmax, ymin, ymax)

    plt.xlim(xmin, xmax)
    plt.ylim(ymin, ymax)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(titulo)
    plt.grid(alpha=0.3)
    plt.show()


def graficar_soluciones(funcion, titulo, xmin, xmax, ymin, ymax, x0, y0):

    plt.figure(figsize=(8, 6))
    campo_pendientes(funcion, xmin, xmax, ymin, ymax)

    # Familia: todas las curvas ancladas en x = x0
    valores = np.linspace(ymin + 1, ymax - 1, 7)

    for valor in valores:
        t, v = resolver(funcion, x0, valor, xmin, xmax)
        plt.plot(t, v, linewidth=1, color="tab:blue", alpha=0.6)

    # Solución particular: ahora sí pasa por (x0, y0)
    t, v = resolver(funcion, x0, y0, xmin, xmax)
    plt.plot(t, v, linewidth=3, color="tab:red", label="Solución particular")

    plt.scatter(x0, y0, s=70, color="black", zorder=5,
                label=f"Condición inicial y({x0}) = {y0}")

    plt.xlim(xmin, xmax)
    plt.ylim(ymin, ymax)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(titulo)
    plt.grid(alpha=0.3)
    plt.legend(loc="best")
    plt.show()


# ==========================================================
# EJERCICIOS
# ==========================================================

# 1(a) y' = -y - sin(x),  y(0) = 1
graficar_campo(f_a, "1(a) Campo: y' = -y - sen(x)", -5, 5, -5, 5)
graficar_soluciones(f_a, "1(a) Familia de soluciones", -5, 5, -5, 5, 0, 1)

# 1(b) y' = x + y,  y(-2) = 2
graficar_campo(f_b, "1(b) Campo: y' = x + y", -5, 5, -5, 5)
graficar_soluciones(f_b, "1(b) Familia de soluciones", -5, 5, -5, 5, -2, 2)

# 1(c) y' = -x^2 + sen(y),  se escoge y(0) = 0
graficar_campo(f_c, "1(c) Campo: y' = -x² + sen(y)", -5, 5, -10, 5)
graficar_soluciones(f_c, "1(c) Familia de soluciones", -5, 5, -10, 5, 0, 0)

# 1(d) (x²+1)y' + 3xy = 6x,  se escoge y(0) = 3
graficar_campo(f_d, "1(d) Campo: y' = (6x - 3xy)/(x² + 1)", -5, 5, -5, 5)
graficar_soluciones(f_d, "1(d) Familia de soluciones", -5, 5, -5, 5, 0, 3)

# 1(e) y' = x·e^y,  se escoge y(0) = 0
graficar_campo(f_e, "1(e) Campo: y' = x·e^y", -1, 1, -5, 5)
graficar_soluciones(f_e, "1(e) Familia de soluciones", -1, 1, -5, 5, 0, 0)

# 1(f) y' = x - y,  y(1) = 1
graficar_campo(f_f, "1(f) Campo: y' = x - y", -5, 5, -5, 5)
graficar_soluciones(f_f, "1(f) Familia de soluciones", -5, 5, -5, 5, 1, 1)
