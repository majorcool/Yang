import random

import pygame
import sys
import os
from scene import Ground
from scene import Cloud


FPS = 60
TITLE = 'Chrome Dino'
BACKGROUND_COLOR = (235, 235, 235)
SCREENSIZE = (700, 300)
IMAGE_PATHS = {
    'ground': 'C:/Users/86153/Desktop/校企联培/作业/PA3/ground.png',
    'cloud': 'resources/images/cloud.png',
}

pygame.init()
screen = pygame.display.set_mode(SCREENSIZE)
pygame.display.set_caption(TITLE)

image_ground = pygame.image.load(IMAGE_PATHS['ground'])
ground = Ground(image_ground, (0, SCREENSIZE[1]))

image_cloud = pygame.image.load(IMAGE_PATHS['cloud'])
cloud_sprites_group = pygame.sprite.Group()

clock = pygame.time.Clock()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BACKGROUND_COLOR)

    pygame.display.update()
    clock.tick(FPS)

    ground.update()
    ground.draw(screen)

    if len(cloud_sprites_group) < 5:
        generate = random.randint(1, 100)
        if generate == 6:
            cloud_sprites_group.add(Cloud(image_cloud, (SCREENSIZE[0], random.randint(20, 70))))

