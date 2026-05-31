import pickle
import easygui as gui
import pygame 
import hormiga_logic as log

tam = 10
filas = 50
columnas = 50

def main():
    pygame.init()
    clock = pygame.time.Clock()
    global tam, filas, columnas

    #Bienvenida

    gui.msgbox(
        msg=   "Bienvenido a la Hormiga de Langton!\n"
               "En este automata una hormiga recorre una matriz y va cambiando\n"
               "los colores de las celdas segun las reglas que usted defina.\n\n"
               "Desarrollado por:\n"
               "Maximiliano Carmiol y Santiago Arrieta",
        title= "Bienvenido a la Hormiga de Langton",
        ok_button= "Quiero jugar!"
    )

    #Cargar automata o crear nuevo

    eleccion_inicio = gui.buttonbox(
        msg = "Tiene un automata guardado que desee utilizar?",
        title = "Inicio",
        choices = ("Si, quiero usar mi automata guardado", "No, quiero crear un nuevo automata" \
        )

        if eleccion_inicio == "Si, quiero usar mi automata guardado":
            loop = True
            while loop:
                ruta = gui.fileopenbox(
                    msg = "Seleccione el archivo de su automata guardado",
                    title = "Cargar Hormiga de Langton",
                )
                if ruta is None:
                eleccion = gui.buttonbox(
                    msg=    "No selecciono ningun archivo",
                    title=  "Sin archivo seleccionado",
                    choices= ("Intentar otra vez", "No quiero cargar")
                )
                if eleccion == "No quiero cargar":
                    loop = False
                else:
                    try:
                        archivo = open(ruta, "rb")
                        datos   = pickle.load(archivo)
                        archivo.close()
    
                        matriz = datos["matriz"]
                        filas = datos["filas"]
                        columnas = datos["columnas"]
                        tam = datos["tamaño"]
                        reglas = datos["reglas"]
                        fila_hormiga = datos["fila_hormiga"]
                        columna_hormiga = datos["columna_hormiga"]
                        direccion_hormiga = datos["direccion_hormiga"]
    
                        ancho_ventana = columnas * tam
                        alto_ventana = filas * tam
                        ventana = pygame.display.set_mode((ancho_ventana, alto_ventana))
                        pygame.display.set_caption("Hormiga de Langton")
    
                        loop = False
                    except Exception as e:
                        gui.msgbox(
                        msg=      "Ocurrio un error al cargar el archivo. Intentelo de nuevo.",
                        title=    "Error al cargar",
                        ok_button= "Elegir otro archivo"
                    )
        else:
        
            #Pedir reglas

            loop = True
            while loop:
                reglas = gui.enterbox(
                    msg=     "Ingrese las reglas de la hormiga.\n"
                             "Use solo letras L (izquierda) y R (derecha).\n"
                             "Cada letra representa un color.\n"
                             "Ejemplo: LR es la hormiga original, LLRR genera patrones simetricos.",
                    title=   "Reglas de la hormiga",
                    default= "LR"
                )
            
                if reglas is None or reglas.strip() == "":
                    gui.msgbox(
                        msg=      "Debe ingresar al menos una regla.",
                        title=    "Error en las reglas",
                        ok_button= "Ingresar otra vez"
                    )
    
                elif not all(letra in "LRlr" for letra in reglas):
                    gui.msgbox(
                        msg=      "Las reglas solo pueden contener letras L y R.",
                        title=    "Error en las reglas",
                        ok_button= "Ingresar otra vez"
                    )
    
                else:
                    reglas = reglas.upper()
                    loop   = False
            
            # Pedir la cantidad de filas
            
            loop = True
            while loop:
    
                respuesta_filas = gui.enterbox(
                    msg=     "Cuantas filas desea que tenga la matriz?",
                    title=   "Filas de la matriz",
                    default= "50"
                )
    
                if respuesta_filas is None:
                    gui.msgbox(
                        msg=      "Debe ingresar un valor para las filas.",
                        title=    "Error",
                        ok_button= "Ingresar otra vez"
                    )
    
                elif not respuesta_filas.isdigit():
                    gui.msgbox(
                        msg=      "Debe ingresar un numero entero para las filas.",
                        title=    "Error",
                        ok_button= "Ingresar otra vez"
                    )
    
                elif int(respuesta_filas) < 1 or int(respuesta_filas) > 500:
                    gui.msgbox(
                        msg=      "El valor de las filas debe estar entre 1 y 500.",
                        title=    "Error",
                        ok_button= "Ingresar otra vez"
                    )
    
                else:
                    filas = int(respuesta_filas)
                    loop  = False
    
            
            # Pedir la cantidad de columnas
            
            loop = True
            while loop:
    
                respuesta_columnas = gui.enterbox(
                    msg=     "Cuantas columnas desea que tenga la matriz?",
                    title=   "Columnas de la matriz",
                    default= "50"
                )
    
                if respuesta_columnas is None:
                    gui.msgbox(
                        msg=      "Debe ingresar un valor para las columnas.",
                        title=    "Error",
                        ok_button= "Ingresar otra vez"
                    )
    
                elif not respuesta_columnas.isdigit():
                    gui.msgbox(
                        msg=      "Debe ingresar un numero entero para las columnas.",
                        title=    "Error",
                        ok_button= "Ingresar otra vez"
                    )
    
                elif int(respuesta_columnas) < 1 or int(respuesta_columnas) > 500:
                    gui.msgbox(
                        msg=      "El valor de las columnas debe estar entre 1 y 500.",
                        title=    "Error",
                        ok_button= "Ingresar otra vez"
                    )
    
                else:
                    columnas = int(respuesta_columnas)
                    loop     = False