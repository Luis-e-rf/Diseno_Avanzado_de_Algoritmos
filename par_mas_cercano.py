import random
import math
import time
import copy
import matplotlib.pyplot as plt

# Una clase que representa un punto en 2D


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Función para calcular la distancia entre dos puntos


def calcular_distancia(A, B):
    distancia = math.sqrt((A.x-B.x)*(A.x-B.x) + (A.y-B.y)*(A.y-B.y))
    return distancia

# escribir una funcion que compare todos los puntos entre si


def fuerza_bruta(nube_puntos):
    distancia_ref = math.inf
    for i in range(len(nube_puntos)):
        for j in range(i+1, len(nube_puntos)):
            distancia_menor = calcular_distancia(
                nube_puntos[i], nube_puntos[j])
            if distancia_menor < distancia_ref:
                distancia_ref = distancia_menor
    return distancia_ref


# Función para encontrar la distancia entre los puntos más cercanos de una sección de un tamaño determinado. Todos los puntos se ordenan según la coordenada y. Todos tienen un límite superior en la distancia mínima como d.
def puntos_cercanos(puntos, tamano, d):

    # Inicializa la distancia mínima como d
    min_val = d

    # Elije todos los puntos uno por uno y prueba los siguientes, hasta que la diferencia entre las coordenadas 'y' sea menor que d.
    for i in range(tamano):
        j = i + 1
        while j < tamano and (puntos[j].y -
                              puntos[i].y) < min_val:
            min_val = calcular_distancia(puntos[i], puntos[j])
            j += 1

    return min_val


# Función recursiva para encontrar la distancia más pequeña. La matriz P contiene todos los puntos ordenados según la coordenada x


def puntosMasCercano(P, Q, n):

    # si tiene 2 o 3 puntos, entonces usa la función fuerza bruta
    if n <= 3:
        return fuerza_bruta(P)

    # encuentra el punto medioFind the middle point
    mid = n // 2
    punto_medio = P[mid]

    # guarda una copia de la rama izquierda y derecha
    Pl = P[:mid]
    Pr = P[mid:]

    # Considera la línea vertical que pasa por el punto medio y calcula la distancia más pequeña dl a la izquierda del punto medio y dr en el lado derecho
    dl = puntosMasCercano(Pl, Q, mid)
    dr = puntosMasCercano(Pr, Q, n - mid)

    # Encuentra la menor de dos distancias
    d = min(dl, dr)

    # Construimos dos matrizes [] que contenga puntos cercanos (más cercanos que d) a la línea que pasa por el punto medio
    ArrayP = []
    ArrayQ = []
    lr = Pl + Pr
    for i in range(n):
        if abs(lr[i].x - punto_medio.x) < d:
            ArrayP.append(lr[i])
        if abs(Q[i].x - punto_medio.x) < d:
            ArrayQ.append(Q[i])
    ArrayP.sort(key=lambda point: point.y)  # <-- REQUIRED}
    min_b = min(d, puntos_cercanos(ArrayQ, len(ArrayQ), d))
    min_a = min(d, puntos_cercanos(ArrayP, len(ArrayP), d))

    # Encuentra los puntos más cercanos en cada array. Devuelve el mínimo entre d y los puntos con la distancia más cercana en cada array.
    return min(min_a, min_b)

# La función principal que encuentra la distancia más pequeña


def closest(P):
    n = len(P)
    P.sort(key=lambda point: point.x)
    Q = copy.deepcopy(P)
    Q.sort(key=lambda point: point.y)

    # Usa la función recursiva puntosMasCercano() para encontrar la distancia más pequeña
    return puntosMasCercano(P, Q, n)


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

cordX = [random.randint(-500, 500) for i in range(100)]
cordY = [random.randint(-500, 500) for i in range(100)]
puntos = []
for i in range(len(cordX)):
    puntos.append((Point(cordX[i], cordY[i])))

inicio = time.time()
print("distancia minima entre los dos puntos mas cercanos: ", closest(puntos))
fin = time.time()
plt.xlim(-500, 500)
plt.ylim(-500, 500)
plt.xticks(range(-500, 501, 50))
plt.yticks(range(-500, 501, 50))
plt.scatter(cordX, cordY, s=5)
print("tiempo utilizado: ", fin - inicio)
plt.show()
