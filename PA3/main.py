import random
import pygame
import sys
from obstacle import Ptera
from scene import Ground
from scene import Cloud
from obstacle import Cactus


FPS = 60
TITLE = 'Chrome Dino'
BACKGROUND_COLOR = (235, 235, 235)
SCREENSIZE = (700, 300)
IMAGE_PATHS = {
    'ground': 'C:/Users/86153/Desktop/校企联培/作业/PA3/images/ground.png',
    'cloud': 'C:/Users/86153/Desktop/校企联培/作业/PA3/images/cloud.png',
    'ptera1': 'C:/Users/86153/Desktop/校企联培/作业/PA3/images/pterodactyl1.png',
    'ptera2': 'C:/Users/86153/Desktop/校企联培/作业/PA3/images/pterodactyl2.png',
    'cactus1': 'C:/Users/86153/Desktop/校企联培/作业/PA3/images/Cactus1.png',
    'cactus2': 'C:/Users/86153/Desktop/校企联培/作业/PA3/images/Cactus2.png',
    'cactus3': 'C:/Users/86153/Desktop/校企联培/作业/PA3/images/Cactus3.png',
    'cactus4': 'C:/Users/86153/Desktop/校企联培/作业/PA3/images/Cactus4.png',
    'cactus5': 'C:/Users/86153/Desktop/校企联培/作业/PA3/images/Cactus5.png',
    'cactus6': 'C:/Users/86153/Desktop/校企联培/作业/PA3/images/Cactus6.png',
}

pygame.init()
screen = pygame.display.set_mode(SCREENSIZE)
pygame.display.set_caption(TITLE)

image_ground = pygame.image.load(IMAGE_PATHS['ground'])
ground = Ground(image_ground, (0, SCREENSIZE[1]))

image_cloud = pygame.image.load(IMAGE_PATHS['cloud'])
cloud_sprites_group = pygame.sprite.Group()

image_ptera_0 = pygame.image.load(IMAGE_PATHS['ptera1'])
image_ptera_1 = pygame.image.load(IMAGE_PATHS['ptera2'])
ptera_sprites_group = pygame.sprite.Group()

clock = pygame.time.Clock()

image_cactus_1 = pygame.image.load(IMAGE_PATHS['cactus1'])
image_cactus_2 = pygame.image.load(IMAGE_PATHS['cactus2'])
image_cactus_3 = pygame.image.load(IMAGE_PATHS['cactus3'])
image_cactus_4 = pygame.image.load(IMAGE_PATHS['cactus4'])
image_cactus_5 = pygame.image.load(IMAGE_PATHS['cactus5'])
image_cactus_6 = pygame.image.load(IMAGE_PATHS['cactus6'])
cactus_sprites_group = pygame.sprite.Group()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BACKGROUND_COLOR)

    if len(cloud_sprites_group) < 5:
        generate = random.randint(1, 100)
        if generate == 6:
            cloud_sprites_group.add(Cloud(image_cloud, (SCREENSIZE[0], random.randint(30, 75))))

    if len(cloud_sprites_group) < 1:
        cloud_sprites_group.add(Cloud(image_cloud, (SCREENSIZE[0], random.randint(30, 75))))

    for cloud in cloud_sprites_group:
        if cloud.rect.right <= 0:
            cloud_sprites_group.remove(cloud)

    if len(ptera_sprites_group) < 5:
        generate = random.randint(1, 100)
        if generate == 6:
            ptera_sprites_group.add(Ptera(image_ptera_0, image_ptera_1, (SCREENSIZE[0], random.randint(120, 230))))

    if len(cactus_sprites_group) < 5:
        generate = random.randint(1, 100)
        if generate == 6:
            magnitude = random.choice((image_cactus_1, image_cactus_2, image_cactus_3, image_cactus_4, image_cactus_5, image_cactus_6))
            if magnitude == image_cactus_1:
                cactus_sprites_group.add(Cactus(magnitude, (SCREENSIZE[0], 192)))
            if magnitude in (image_cactus_2, image_cactus_3):
                cactus_sprites_group.add(Cactus(magnitude, (SCREENSIZE[0], 195)))
            if magnitude in (image_cactus_4, image_cactus_5, image_cactus_6):
                cactus_sprites_group.add(Cactus(magnitude, (SCREENSIZE[0], 220)))

    for cactus in cactus_sprites_group:
        if cactus.rect.right <= 0:
            cactus_sprites_group.remove(cactus)

    ground.update()
    cloud_sprites_group.update()
    ptera_sprites_group.update()
    cactus_sprites_group.update()

    ground.draw(screen)
    cloud_sprites_group.draw(screen)
    ptera_sprites_group.draw(screen)
    cactus_sprites_group.draw(screen)

    pygame.display.update()
    clock.tick(FPS)


