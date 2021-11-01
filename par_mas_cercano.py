import math
import time
import random
# escribir una funcion para calcular la distancia entre dos puntos


def calcular_distancia(A, B):
    distancia = math.sqrt((B[0]-A[0])**2 + (A[1]-B[1])**2)
    return distancia

# escribir una funcion que compare todos los puntos entre si
# puntos = [(2, 3), (7, 2), (1, 0), (-4, 8), (-3, -9), (0, 0), (-1, -5)]
cordX = [random.randint(-500, 500) for i in range(3000)]
cordY = [random.randint(-500, 500) for i in range(3000)]
puntos = []
for i in range(len(cordX)):
    puntos.append((cordX[i], cordY[i]))


def puntos_cercanos(nube_puntos):
    distancia_ref = math.inf
    for i in range(len(nube_puntos)):
        for j in range(i+1, len(nube_puntos)):
            distancia_menor = calcular_distancia(
                nube_puntos[i], nube_puntos[j])
            if distancia_menor < distancia_ref:
                distancia_ref = distancia_menor
                par_cercano = (nube_puntos[i], nube_puntos[j])
    return distancia_ref, par_cercano


inicio = time.time()
par = puntos_cercanos(puntos)
fin = time.time()
print(fin - inicio)
print(par)
