import math
import time
import random
import matplotlib.pyplot as plt
# escribir una funcion para calcular la distancia entre dos puntos


def calcular_distancia(A, B):
    distancia = math.sqrt((B[0]-A[0])**2 + (A[1]-B[1])**2)
    return distancia


# escribir una funcion que compare todos los puntos entre si
# puntos = [(2, 3), (7, 2), (1, 0), (-4, 8), (-3, -9), (0, 0), (-1, -5)]
cordX = [random.randint(-500, 500) for i in range(100)]
cordY = [random.randint(-500, 500) for i in range(100)]
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
    return "La distancia minima entre los dos puntos es: ", distancia_ref, ". Y los puntos demarcados son: ", par_cercano


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')


inicio = time.time()
par = puntos_cercanos(puntos)
fin = time.time()
print("tiempo utilizado: ", fin - inicio)
print(par)
plt.xlim(-500, 500)
plt.ylim(-500, 500)
plt.xticks(range(-500, 501, 50))
plt.yticks(range(-500, 501, 50))
plt.scatter(cordX, cordY, s=5)
x = [par[3][0][0], par[3][1][0]]
y = [par[3][0][1], par[3][1][1]]
plt.plot(x, y, 'r')
plt.show()
