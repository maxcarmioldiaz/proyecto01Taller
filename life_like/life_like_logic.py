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
   
   """
   filas = len(M)
   columnas = len(M[0])
   vecinos = []
   for fv in range(f-1, f+2):
       for cv in range(c-1, c+2):
           if fv != f or cv != c:
               vecinos.append(M[fv % filas][cv % columnas])
   return vecinos

def parametros(P):
    P = str(P)
    P = list(P)
    for i in range(P):
         P[i] = int(P[i])
    return P


def transicion_celula(estado, vecinos, B, S):
    """
    Funcion que toma el estado de una celula y la de todos 
    sus vecinos e indica el estado final en el que tiene que estar segun
    los parametros para estar viva o que nazcan nuevas.
    Entradas:
        -estado, valor de la celula a transicionar puede ser un 0 o 1
        -vecinos, el valor (estado) de los vecinos puede ser un 0 o 1
        -B, parametro que indica en que situaciones puede nacer una nueva celular es decir pasar de 0 a 1
        -S, parametro que indica en que situaciones se mantienen vivas las celulas, es decir, mantenerse en 1
    Salidas:
        -estado de la celula a transicionar segun los parametros indicados (0 o 1)
    Restricciones:
        -estado debe ser un 0 o 1
        -vecinos deben ser 0 o 1
        -B
        -S
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

def transicion(M):
    """
    
    """
    new = []
    for f in range(len(M)):
       fila = []
       for c in range(len(M[0])):
           vecinos = obtener_vecinos(M, f, c)
           celula = transicion_celula(M[f][c], vecinos)
           fila.append(celula)
       new.append(fila)
    return new
 
