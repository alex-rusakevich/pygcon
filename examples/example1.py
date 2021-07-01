from pygcon import main as pgcm
import pygame

pygame.font.init()
font = pygame.font.SysFont("couriernew", 18)

matrix_size = (80, 20)
console_window = pgcm.Main_Application(font, matrix_size)
console_window.start()
