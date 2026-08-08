import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


# Ecuación diferencial

def poblacion(t, P):
    return P * (P - 1) * (2 - P)


# Puntos críticos

puntos_criticos = [0, 1, 2]

print("PUNTOS CRÍTICOS")

for punto in puntos_criticos:
    print("P =", punto)


# Análisis del signo

print("\nDIAGRAMA DE FASE")
print()

print("P < 0       :  P' > 0   ↑")
print("0 < P < 1   :  P' < 0   ↓")
print("1 < P < 2   :  P' > 0   ↑")
print("P > 2       :  P' < 0   ↓")


# Población inicial

P0 = float(input("\nIngrese la población inicial en miles: "))


# Resolver la ecuación diferencial

tiempo = np.linspace(0, 10, 500)

solucion = solve_ivp(
    poblacion,
    [0, 10],
    [P0],
    t_eval=tiempo
)


# Gráfica de la solución

plt.figure(figsize=(9, 6))

plt.plot(
    solucion.t,
    solucion.y[0],
    linewidth=2,
    label="Población"
)

# Líneas de equilibrio

plt.axhline(0, linestyle="--", label="P = 0")
plt.axhline(1, linestyle="--", label="P = 1")
plt.axhline(2, linestyle="--", label="P = 2")

plt.xlabel("Tiempo (años)")
plt.ylabel("Población (miles)")

plt.title("Modelo de población")

plt.grid()
plt.legend()

plt.show()


# Análisis de la población inicial

if P0 < 0:

    print("\nLa población aumenta.")

elif P0 == 0:

    print("\nLa población permanece en P = 0.")

elif P0 < 1:

    print("\nLa población disminuye y tiende a 0.")

elif P0 == 1:

    print("\nLa población permanece en P = 1.")

elif P0 < 2:

    print("\nLa población aumenta y tiende a 2.")

elif P0 == 2:

    print("\nLa población permanece en P = 2.")

else:

    print("\nLa población disminuye y tiende a 2.")
