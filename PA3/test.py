import pygame
import sys

pygame.init()

size = width, height = 800, 600

screen = pygame.display.set_mode(size)

pygame.display.set_caption('game')
object1 = pygame.font.SysFont('宋体', 50)
text = object1.render('hellow world', True, (0, 0, 255))
screen.blit(text, (300, 300))

while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            sys.exit()

    pygame.display.update()