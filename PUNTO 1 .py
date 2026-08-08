import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


# Funciones de las ecuaciones diferenciales

def ecuacion_a(x, y):
    return -y - np.sin(x)


def ecuacion_b(x, y):
    return x + y


def ecuacion_c(x, y):
    return -x**2 + np.sin(y)


def ecuacion_d(x, y):
    return (6*x - 3*x*y)/(x**2 + 1)


def ecuacion_e(x, y):
    return x*np.exp(y)


def ecuacion_f(x, y):
    return x - y


# Función para dibujar el campo de pendientes

def campo_pendientes(funcion, xmin, xmax, ymin, ymax):
    
    x = np.linspace(xmin, xmax, 20)
    y = np.linspace(ymin, ymax, 20)

    X, Y = np.meshgrid(x, y)

    M = funcion(X, Y)

    U = np.ones_like(M)
    V = M

    magnitud = np.sqrt(U**2 + V**2)

    U = U / magnitud
    V = V / magnitud

    plt.quiver(X, Y, U, V)


# Selección del ejercicio

print("PUNTO 1 - ECUACIONES DIFERENCIALES")
print("1. y' = -y - sin(x)")
print("2. y' = x + y")
print("3. y' = -x^2 + sin(y)")
print("4. (x^2 + 1)y' + 3xy = 6x")
print("5. y' = x e^y")
print("6. y' = x - y")

opcion = int(input("Seleccione el ejercicio: "))


if opcion == 1:

    funcion = ecuacion_a
    x0 = 0
    y0 = 1
    xmin = -5
    xmax = 5
    ymin = -5
    ymax = 5

elif opcion == 2:

    funcion = ecuacion_b
    x0 = -2
    y0 = 2
    xmin = -5
    xmax = 5
    ymin = -5
    ymax = 5

elif opcion == 3:

    funcion = ecuacion_c
    x0 = 0
    y0 = 0
    xmin = -5
    xmax = 5
    ymin = -10
    ymax = 5

elif opcion == 4:

    funcion = ecuacion_d
    x0 = 0
    y0 = 3
    xmin = -5
    xmax = 5
    ymin = -5
    ymax = 5

elif opcion == 5:

    funcion = ecuacion_e
    x0 = 0
    y0 = 0
    xmin = -1
    xmax = 1
    ymin = -5
    ymax = 5

elif opcion == 6:

    funcion = ecuacion_f
    x0 = 1
    y0 = 1
    xmin = -5
    xmax = 5
    ymin = -5
    ymax = 5

else:

    print("Opción no válida")
    exit()


# Crear la gráfica

plt.figure(figsize=(9, 7))

campo_pendientes(funcion, xmin, xmax, ymin, ymax)


# Soluciones que pasan por diferentes puntos

puntos = [-3, -2, -1, 0, 1, 2, 3]

for valor in puntos:

    solucion = solve_ivp(
        funcion,
        [xmin, xmax],
        [valor],
        t_eval=np.linspace(xmin, xmax, 400)
    )

    plt.plot(solucion.t, solucion.y[0])


# Solución particular

solucion_particular = solve_ivp(
    funcion,
    [xmin, xmax],
    [y0],
    t_eval=np.linspace(xmin, xmax, 400)
)

plt.plot(
    solucion_particular.t,
    solucion_particular.y[0],
    linewidth=3,
    label="Solución particular"
)

plt.scatter(x0, y0, s=50, label="Condición inicial")

plt.xlim(xmin, xmax)
plt.ylim(ymin, ymax)

plt.xlabel("x")
plt.ylabel("y")

plt.title("Campo de pendientes y soluciones")

plt.grid()
plt.legend()

plt.show()
