import pygame
import sys

screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
screen.fill((255, 255, 255))

graph = (1, 2, 3)
pygame.display.set_icon()
pygame.display.set_caption('game')

while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            sys.exit()

    pygame.display.update()