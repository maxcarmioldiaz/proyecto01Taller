import pickle
import easygui
import pygame
import life_like_logic as log

tam = 10
filas = 50
columnas = 50
tick = 10

def main():
    pygame.init()
    clock = pygame.time.Clock()
    
    M = log.generar_matriz_aleatoria