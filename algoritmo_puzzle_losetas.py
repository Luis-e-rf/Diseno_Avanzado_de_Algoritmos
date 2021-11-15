from simpleai.search import astar, SearchProblem

#Busqueda en Profundidad

META = '''1-2-3
4-5-6
7-8-e'''

INICIO = '''4-5-1
8-3-7
e-6-2'''


def list_string(list_):
    return '\n'.join(['-'.join(row) for row in list_])


def string_list(string_):
    return [row.split('-') for row in string_.split('\n')]


def encontrar_lugar(rows, element_to_find):
    '''Encuentra la direccion de la ficha buscada y devuelve fila, columna'''
    for ir, row in enumerate(rows):
        for ic, element in enumerate(row):
            if element == element_to_find:
                return ir, ic


#Se guarda la posicion final de cada pieza, para no tener que recalcular en cada ciclo
posiciones_meta = {}
rows_meta = string_list(META)
for num in '12345678e':
    posiciones_meta[num] = encontrar_lugar(rows_meta, num)


class Puzzle(SearchProblem):
    def actions(self, estado):
        '''Retorna una lista de las piezas que podemos mover a un espacio vacio'''
        rows = string_list(estado)
        row_e, col_e = encontrar_lugar(rows, 'e')

        acciones = []
        if row_e > 0:
            acciones.append(rows[row_e - 1][col_e])
        if row_e < 2:
            acciones.append(rows[row_e + 1][col_e])
        if col_e > 0:
            acciones.append(rows[row_e][col_e - 1])
        if col_e < 2:
            acciones.append(rows[row_e][col_e + 1])

        return acciones

    def result(self, estado, accion):
        '''retorna el estado resultante despues de mover una ficha a un espacio vacio. El parametro accion contiene la pieza a mover'''
        rows = string_list(estado)
        row_e, col_e = encontrar_lugar(rows, 'e')
        row_n, col_n = encontrar_lugar(rows, accion)

        rows[row_e][col_e], rows[row_n][col_n] = rows[row_n][col_n], rows[row_e][col_e]

        return list_string(rows)

    def is_goal(self, estado):
        '''Devuelve true si el estado actual es el estado deseado'''
        return estado == META
     
    def heuristic(self, estado):
        '''Retorna una estimacion de la distancia al estado deseado usando la distancia manhatan'''
        rows = string_list(estado)

        distancia = 0

        for num in '12345678e':
            row_n, col_n = encontrar_lugar(rows, num)
            row_n_goal, col_n_goal = posiciones_meta[num]

            distancia += abs(row_n - row_n_goal) + abs(col_n - col_n_goal)

        return distancia


result = astar(Puzzle(INICIO))


for accion, estado in result.path():
    print ('Mueve el numero ', accion)
    print (estado)