from random import randint

def girar_hormiga(direccion_actual, giro):
    """
    Funcion que actualiza la direccion de la hormiga segun el giro indicado.
    Entradas:
        -direccion_actual, string con la direccion en la que apunta la hormiga,
            puede ser 'arriba', 'abajo', 'izquierda' o 'derecha'
        -giro, caracter que indica hacia donde girar,
            'R' para girar a la derecha, 'L' para girar a la izquierda
    Salidas:
        -string con la nueva direccion de la hormiga despues del giro
    Restricciones:
        -direccion_actual debe ser 'arriba', 'abajo', 'izquierda' o 'derecha'
        -giro debe ser 'L' o 'R'
    """
    if giro == "R":
        if direccion_actual == "arriba":
            nueva_direccion = "derecha"
        elif direccion_actual == "derecha":
            nueva_direccion = "abajo"
        elif direccion_actual == "abajo":
            nueva_direccion = "izquierda"
        else:
            nueva_direccion = "arriba"
 
    else:
        if direccion_actual == "arriba":
            nueva_direccion = "izquierda"
        elif direccion_actual == "izquierda":
            nueva_direccion = "abajo"
        elif direccion_actual == "abajo":
            nueva_direccion = "derecha"
        else:
            nueva_direccion = "arriba"
 
    return nueva_direccion

def avanzar_hormiga(fila_actual, columna_actual, direccion_actual, total_filas, total_columnas):
    """
    Funcion que mueve la hormiga una celda hacia adelante segun su direccion actual.
    Si la hormiga llega al borde de la matriz, aparece en el lado opuesto (wrap-around).
    Entradas:
        -fila_actual, entero con la fila donde esta parada la hormiga
        -columna_actual, entero con la columna donde esta parada la hormiga
        -direccion_actual, string con la direccion en la que apunta la hormiga
        -total_filas, entero positivo con la cantidad de filas de la matriz
        -total_columnas, entero positivo con la cantidad de columnas de la matriz
    Salidas:
        -tupla (nueva_fila, nueva_columna) con la posicion de la hormiga despues de avanzar
    Restricciones:
        -fila_actual debe ser un entero entre 0 y total_filas - 1
        -columna_actual debe ser un entero entre 0 y total_columnas - 1
        -direccion_actual debe ser 'arriba', 'abajo', 'izquierda' o 'derecha'
        -total_filas y total_columnas deben ser enteros positivos
    """
    if direccion_actual == "arriba":
        nueva_fila = (fila_actual - 1) % total_filas
        nueva_columna = columna_actual
    elif direccion_actual == "abajo":
        nueva_fila = (fila_actual + 1) % total_filas
        nueva_columna = columna_actual
    elif direccion_actual == "izquierda":
        nueva_fila = fila_actual
        nueva_columna = (columna_actual - 1) % total_columnas
    else:  # direccion_actual == "derecha"
        nueva_fila = fila_actual
        nueva_columna = (columna_actual + 1) % total_columnas

    return (nueva_fila, nueva_columna)

def siguiente(matriz, fila_hormiga, columna_hormiga, direccion_hormiga, reglas):
    """
    Funcion que ejecuta un paso del automata de la hormiga de Langton:
        1. Lee el color de la celda donde esta la hormiga
        2. Gira segun la regla que corresponde a ese color
        3. Cambia el color de la celda al siguiente color de forma ciclica
        4. Avanza la hormiga una celda en la nueva direccion
    Entradas:
        -matriz, matriz bidimensional de enteros donde cada valor es un
            indice de color (entre 0 y cantidad_colores - 1)
        -fila_hormiga, entero con la fila actual de la hormiga
        -columna_hormiga, entero con la columna actual de la hormiga
        -direccion_hormiga, string con la direccion actual de la hormiga
        -reglas, string con caracteres 'L' y 'R'; su longitud indica cuantos
            colores hay, y cada posicion indica que giro hace la hormiga
            cuando esta sobre ese color (ejemplo: "LR" -> 2 colores)
    Salidas:
        -tupla (matriz, fila_hormiga, columna_hormiga, direccion_hormiga)
            con todos los valores actualizados despues del paso
    Restricciones:
        -matriz debe tener valores enteros entre 0 y len(reglas) - 1
        -fila_hormiga y columna_hormiga deben ser indices validos en la matriz
        -direccion_hormiga debe ser 'arriba', 'abajo', 'izquierda' o 'derecha'
        -reglas debe ser un string no vacio con solo caracteres 'L' y 'R'
    """
    cantidad_colores = len(reglas)
    color_celda_actual = matriz[fila_hormiga][columna_hormiga]
 
    #  girar segun la regla del color actual
    giro_a_realizar = reglas[color_celda_actual]
    direccion_hormiga = girar_hormiga(direccion_hormiga, giro_a_realizar)
 
    #  cambiar el color de la celda al siguiente 
    matriz[fila_hormiga][columna_hormiga] = (color_celda_actual + 1) % cantidad_colores
 
    # avanzar la hormiga una celda
    total_filas    = len(matriz)
    total_columnas = len(matriz[0])
    fila_hormiga, columna_hormiga = avanzar_hormiga(
        fila_hormiga, columna_hormiga,
        direccion_hormiga,
        total_filas, total_columnas
    )

    return (matriz, fila_hormiga, columna_hormiga, direccion_hormiga)

def generar_colores(cantidad_colores):
    """
    Funcion que genera una lista de colores distintos en formato RGB
    tomando los primeros cantidad_colores de una lista de colores predefinidos.
    Entradas:
        -cantidad_colores, entero positivo con la cantidad de colores a generar
    Salidas:
        -lista de tuplas (rojo, verde, azul) con los primeros cantidad_colores
            colores de la lista predefinida
    Restricciones:
        -cantidad_colores debe ser un entero positivo mayor o igual a 1
        -cantidad_colores no debe superar la cantidad de colores en la lista predefinida
    """
    lista_colores = [ (randint(0,255) , randint(0,255) , randint(0,255)) for x in range(cantidad_colores)]
    return lista_colores
