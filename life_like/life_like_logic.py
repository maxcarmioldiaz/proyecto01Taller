from random import randint


def generar_matriz_aleatoria(filas, columnas):
    """
    Funcion que genera una matriz con filas y columnas con 0s y 1s
    aleatoriamente.
    Entradas:
        -filas, entero positivo
        -columnas, entero positivo
    Salidas:
        -Matriz con las dimensiones indicadas en las filas y columnas
        con valores de 0s y 1s.
    Restricciones:
        -Filas debe ser un entero
        -Filas debe ser positivo
        -Columnas debe ser un entero
        -Columnas debe ser positivo
    """
    return [[randint(0 , 1) for c in range(columnas)] for f in range(filas)]

def generar_matriz_vacia(filas, columnas):
    """
    Funcion que genera una matriz con filas y columnas 
    con solo 0s.
    Entradas:
        -filas, entero positivo
        -columnas, entero positivo
    Salidas:
        -Matriz con las dimensiones indicadas en las filas y columnas
        con solo 0s
    Restricciones:
        -Filas debe ser un numero entero
        -Filas debe ser un numero positivo
        -Columnas debe ser un entero
        -Columnas debe ser positivo
    """
    return [[0 for c in range(columnas)] for f in range(filas)]

def obtener_vecinos(M, f, c):
   """
   Funcion que segun la posicion [f][c] de la celula que se este revisando,
   toma el estado sus vecinos es decir las 8 celulas alrededor y estos
   estados se agregan a una lista llamada vecinos la cual es finalmente 
   retornada.
   Entradas:
        -M, es la matriz en la que se encuentran las celulas, los unicos posibles
            valores son 0s y 1s
        -f, se refiere a la fila en la que se encuentra la celula a evaluar, es un 
            numero entero positivo
        -c, se refiere a la columna en la que se encuentra la celula a evaluar, es un
            numero entero positivo
    Salidas:
        -lista de con los estados de los vecinos de la celula que se esta revisando
   """
   filas = len(M)
   columnas = len(M[0])
   vecinos = []
   for fv in range(f-1, f+2):
       for cv in range(c-1, c+2):
           if fv != f or cv != c:
               vecinos.append(M[fv % filas][cv % columnas])
   return vecinos

def transicion_celula(estado, vecinos, B, S):
    """
    Funcion que toma el estado de una celula y la de todos 
    sus vecinos e indica el estado final en el que tiene que estar segun
    los parametros para estar viva o que nazcan nuevas.
    Entradas:
        -estado, valor de la celula a transicionar puede ser un 0 o 1
        -vecinos, el valor (estado) de los vecinos puede ser un 0 o 1
        -B, parametro que indica en que situaciones puede nacer una nueva celular es decir pasar de 0 a 1, 
                es una lista con las cantidades de vecinos vivos que deben haber en la celula muerta a evaluar
                para que nazca una nueva celula
        -S, parametro que indica en que situaciones se mantienen vivas las celulas, es decir, mantenerse en 1,
                es una lista con las cantidades de vecinos vivos que deben haber en la celula viva a evaluar para 
                que esta se mantenga viva
    Salidas:
        -estado de la celula a transicionar segun los parametros indicados (0 o 1)
    Restricciones:
        -estado debe ser un 0 o 1
        -vecinos deben ser 0 o 1
        -B debe ser una lista con numeros enteros positivos
        -S debe ser una lista con numero enteros positivos
    """
    vivos = 0
    for vecino in vecinos:
       if vecino == 1:
           vivos += 1
    if estado == 0 and vivos in B:
       return 1
    if estado == 1 and vivos not in S:
       return 0
    else:
        return estado

def transicion(M, B, S):
    """
    Funcion que revisa celula por celula, toma sus vecinos, cambia sus estados
    y crea una nueva matriz con los estados de cada una de las celulas.
    Entradas:
        -M, matriz con 0s o 1s, es la matriz donde se encuentran las celulas antes del 
        cambio.
        -B, lista numerica con las cantidades de vecinos vivos necesarios para que nazca una nueva
            celula.
        -S, lista numerica con las cantidades de vecinos vivos necesarios para que se mantenga viva
            una celula.
    Salidas:
        -Matriz con los nuevos estados de todas las celulas
    """
    new = []
    for f in range(len(M)):
       fila = []
       for c in range(len(M[0])):
           vecinos = obtener_vecinos(M, f, c)
           celula = transicion_celula(M[f][c], vecinos, B, S)
           fila.append(celula)
       new.append(fila)
    return new
 
