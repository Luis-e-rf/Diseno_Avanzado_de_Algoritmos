
#tamano = int(input("Ingrese el tamaño de la matriz: "))

# Función para definir los valores ingresados


def valores():
    global solucion
    cordX = cordY = 0
    solucion += 1
    for cordX in range(tamano):
        for cordY in range(tamano):
            if cordX == ListaReinas[cordY]:
                ListaReinas[cordX] = solucion


# definir funcion para los bloqueos
solucion = 0
tamano = 4


def bloqueos(fila, columna):
    ListaReinas = []
    i = 0
    ataque = 0  # Si es igual a 0 no se ataca, si es 1 esta bajo ataque
    filaCero = 0
    columnaCero = 0

    while (ataque != 1):
        filaCero = abs(ListaReinas[i]-fila)
        columnaCero = abs(i-columna)
        if ListaReinas[i] == fila or filaCero == columnaCero:
            ataque = 1
        i += 1
        return ataque

# Definir la casilla del tablero


def casilla(value):
    i = 0
    ListaReinas = []
    while i < tamano:
        if bloqueos(i, value) != 1:
            ListaReinas[value] = i+1
            if value == tamano-1:
                # Llamar una función para definir los valores ingresados
                valores()
            else:
                casilla(value+1)
        i += 1


ListaReinas = [None]*tamano
bloqueos(1,3)
