import random

import pygame
import sys
from obstacle import Ptera
from scene import Ground
from scene import Cloud
from obstacle import Cactus
from scoreboard import Scoreboard
from dinosaur import Dinosaur
from set_system import Pause
from set_system import GameOver


FPS = 60
TITLE = 'Chrome Dino'
BACKGROUND_COLOR = (235, 235, 235)
SCREENSIZE = (700, 300)
pygame.init()
screen = pygame.display.set_mode(SCREENSIZE)
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()
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
    '0': 'C:/Users/86153/Desktop/校企联培/作业/PA3/images/scoreboard-0.png',
    '1': 'C:/Users/86153/Desktop/校企联培/作业/PA3/images/scoreboard-1.png',
    '2': 'C:/Users/86153/Desktop/校企联培/作业/PA3/images/scoreboard-2.png',
    '3': 'C:/Users/86153/Desktop/校企联培/作业/PA3/images/scoreboard-3.png',
    '4': 'C:/Users/86153/Desktop/校企联培/作业/PA3/images/scoreboard-4.png',
    '5': 'C:/Users/86153/Desktop/校企联培/作业/PA3/images/scoreboard-5.png',
    '6': 'C:/Users/86153/Desktop/校企联培/作业/PA3/images/scoreboard-6.png',
    '7': 'C:/Users/86153/Desktop/校企联培/作业/PA3/images/scoreboard-7.png',
    '8': 'C:/Users/86153/Desktop/校企联培/作业/PA3/images/scoreboard-8.png',
    '9': 'C:/Users/86153/Desktop/校企联培/作业/PA3/images/scoreboard-9.png',
    '10': 'C:/Users/86153/Desktop/校企联培/作业/PA3/images/scoreboard-10.png',
    'dinosaur0': 'C:/Users/86153/Desktop/校企联培/作业/PA3/images/dinosaur1.png',
    'dinosaur1': 'C:/Users/86153/Desktop/校企联培/作业/PA3/images/dinosaur2.png',
    'dinosaur2': 'C:/Users/86153/Desktop/校企联培/作业/PA3/images/dinosaur-die-1.png',
    'dinosaur3': 'C:/Users/86153/Desktop/校企联培/作业/PA3/images/dinosaur-die-2.png',
    'dinosaur4': 'C:/Users/86153/Desktop/校企联培/作业/PA3/images/dinosaur-duck-1.png',
    'dinosaur5': 'C:/Users/86153/Desktop/校企联培/作业/PA3/images/dinosaur-duck-2.png',
    'dinosaur6': 'C:/Users/86153/Desktop/校企联培/作业/PA3/images/dinosaur-jump.png',
    'dinosaur7': 'C:/Users/86153/Desktop/校企联培/作业/PA3/images/dinosaur-start.png',
    'restart1': 'C:/Users/86153/Desktop/校企联培/作业/PA3/images/restart-1.png',
    'restart2': 'C:/Users/86153/Desktop/校企联培/作业/PA3/images/restart-2.png',
    'restart3': 'C:/Users/86153/Desktop/校企联培/作业/PA3/images/restart-3.png',
    'restart4': 'C:/Users/86153/Desktop/校企联培/作业/PA3/images/restart-4.png',
    'restart5': 'C:/Users/86153/Desktop/校企联培/作业/PA3/images/restart-5.png',
    'restart6': 'C:/Users/86153/Desktop/校企联培/作业/PA3/images/restart-6.png',
    'restart7': 'C:/Users/86153/Desktop/校企联培/作业/PA3/images/restart-7.png',
    'restart8': 'C:/Users/86153/Desktop/校企联培/作业/PA3/images/restart-8.png',
    'game_over': 'C:/Users/86153/Desktop/校企联培/作业/PA3/images/game-over.png'
}

image_ground = pygame.image.load(IMAGE_PATHS['ground'])
ground = Ground(image_ground, (0, SCREENSIZE[1]))

image_cloud = pygame.image.load(IMAGE_PATHS['cloud'])
cloud_sprites_group = pygame.sprite.Group()

image_ptera_0 = pygame.image.load(IMAGE_PATHS['ptera1'])
image_ptera_1 = pygame.image.load(IMAGE_PATHS['ptera2'])
ptera_sprites_group = pygame.sprite.Group()

image_dinosaur_0 = pygame.image.load((IMAGE_PATHS['dinosaur0']))
image_dinosaur_1 = pygame.image.load((IMAGE_PATHS['dinosaur1']))
image_dinosaur_2 = pygame.image.load((IMAGE_PATHS['dinosaur2']))
image_dinosaur_3 = pygame.image.load((IMAGE_PATHS['dinosaur3']))
image_dinosaur_4 = pygame.image.load((IMAGE_PATHS['dinosaur4']))
image_dinosaur_5 = pygame.image.load((IMAGE_PATHS['dinosaur5']))
image_dinosaur_6 = pygame.image.load((IMAGE_PATHS['dinosaur6']))
image_dinosaur_7 = pygame.image.load((IMAGE_PATHS['dinosaur7']))
image_dinosaur = list()
image_dinosaur.append(image_dinosaur_0)
image_dinosaur.append(image_dinosaur_1)
image_dinosaur.append(image_dinosaur_2)
image_dinosaur.append(image_dinosaur_3)
image_dinosaur.append(image_dinosaur_4)
image_dinosaur.append(image_dinosaur_5)
image_dinosaur.append(image_dinosaur_6)
image_dinosaur.append(image_dinosaur_7)
dinosaur = Dinosaur(image_dinosaur, (0, SCREENSIZE[1]-11))

image_cactus_1 = pygame.image.load(IMAGE_PATHS['cactus1'])
image_cactus_2 = pygame.image.load(IMAGE_PATHS['cactus2'])
image_cactus_3 = pygame.image.load(IMAGE_PATHS['cactus3'])
image_cactus_4 = pygame.image.load(IMAGE_PATHS['cactus4'])
image_cactus_5 = pygame.image.load(IMAGE_PATHS['cactus5'])
image_cactus_6 = pygame.image.load(IMAGE_PATHS['cactus6'])
cactus_sprites_group = pygame.sprite.Group()

image_scoreboard = list()
for i in range(0, 11):
    image_scoreboard.append(pygame.image.load(IMAGE_PATHS[str(i)]))
scoreboard = Scoreboard(image_scoreboard, (SCREENSIZE[0], 0))

image_restart = list()
for i in range(1, 9):
    image_restart.append(pygame.image.load(IMAGE_PATHS['restart{}'.format(i)]))
restart = Pause(image_restart, (350, 150))

game_over_image = pygame.image.load(IMAGE_PATHS['game_over'])
game_over = GameOver(game_over_image)

process = 'begin'
refresh_obstacle = 50
refresh_obstacle_count = 0
refresh_cloud = 50
refresh_cloud_count = 0
up_speed = -10
broadcasting = None
prepare_jump = False
repeat = True

if process == 'begin':
    dinosaur.rect.top += 0

while process == 'begin':

    dinosaur.start()
    dinosaur.draw(screen)
    pygame.display.update()
    clock.tick(FPS)
    screen.fill(BACKGROUND_COLOR)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        key_list = pygame.key.get_pressed()

        if key_list[pygame.K_SPACE] or key_list[pygame.K_UP] and dinosaur.state == "begin":
            up_speed -= 3
            up_speed = max(-20, up_speed)

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP or event.key == pygame.K_SPACE and dinosaur.state == "begin":
                broadcasting = "jump"
                prepare_jump = True

        elif event.type == pygame.KEYUP:

            if broadcasting == "jump" and prepare_jump and not dinosaur.state == "jump":
                dinosaur.image = dinosaur.images[0]
                dinosaur.jump(up_speed)
                up_speed = -10
                prepare_jump = False
                process = "start"

if process == 'start':
    dinosaur.rect.top -= 0

while repeat:

    while process == 'start':

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                with open('data/high_score.py', 'w') as f:
                    if scoreboard.high_score < scoreboard.score:
                        f.write(str(scoreboard.score))
                    else:
                        f.write(str(scoreboard.high_score))
                repeat = False
                pygame.quit()
                sys.exit()

            key_list = pygame.key.get_pressed()

            if key_list[pygame.K_SPACE] or key_list[pygame.K_UP] and dinosaur.state == "run":
                up_speed -= 3
                up_speed = max(-20, up_speed)

            if key_list[pygame.K_DOWN] and dinosaur.state == "run" and not prepare_jump:
                dinosaur.duck()

            if key_list[pygame.K_DOWN] and dinosaur.state == "jump":
                dinosaur.up_speed = 20

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_UP or event.key == pygame.K_SPACE and dinosaur.state == "run":
                    broadcasting = "jump"
                    prepare_jump = True

            elif event.type == pygame.KEYUP:

                if broadcasting == "jump" and prepare_jump and not dinosaur.state == "jump":
                    dinosaur.jump(up_speed)
                    up_speed = -10
                    prepare_jump = False

                if dinosaur.state == "duck" and not key_list[pygame.K_DOWN]:
                    dinosaur.unduck()

        screen.fill(BACKGROUND_COLOR)

        if len(cloud_sprites_group) < 5 and refresh_cloud_count >= refresh_cloud:
            generate = random.randint(1, 100)
            if generate == 1:
                cloud_sprites_group.add(Cloud(image_cloud, (SCREENSIZE[0], random.randint(30, 75))))
                refresh_cloud_count = 0
        refresh_cloud_count += 1

        if len(cloud_sprites_group) < 1:
            cloud_sprites_group.add(Cloud(image_cloud, (SCREENSIZE[0], random.randint(30, 75))))

        for cloud in cloud_sprites_group:
            if cloud.rect.right <= 0:
                cloud_sprites_group.remove(cloud)

        if len(ptera_sprites_group) < 5 and refresh_obstacle_count >= refresh_obstacle:
            generate = random.randint(1, 100)
            if generate == 6:
                ptera_sprites_group.add(Ptera(image_ptera_0, image_ptera_1, (SCREENSIZE[0], random.randint(120, 235))))
                refresh_obstacle_count = 0

        if len(cactus_sprites_group) < 5 and refresh_obstacle_count >= refresh_obstacle:
            generate = random.randint(1, 50)
            if generate == 6:
                magnitude = random.choice((image_cactus_1, image_cactus_2, image_cactus_3, image_cactus_4, image_cactus_5, image_cactus_6))
                refresh_obstacle_count = 0
                if magnitude == image_cactus_1:
                    cactus_sprites_group.add(Cactus(magnitude, (SCREENSIZE[0], 192)))
                if magnitude in (image_cactus_2, image_cactus_3):
                    cactus_sprites_group.add(Cactus(magnitude, (SCREENSIZE[0], 195)))
                if magnitude in (image_cactus_4, image_cactus_5, image_cactus_6):
                    cactus_sprites_group.add(Cactus(magnitude, (SCREENSIZE[0], 220)))
        refresh_obstacle_count += 1

        for cactus in cactus_sprites_group:
            if cactus.rect.right <= 0:
                cactus_sprites_group.remove(cactus)

        scoreboard.score = ground.distance//50
        if scoreboard.score and not scoreboard.score % 100:
            pygame.mixer.Sound('C:/Users/86153/Desktop/校企联培/作业/PA3/audios/score.mp3').play()

        ground.update()
        cloud_sprites_group.update()
        ptera_sprites_group.update()
        cactus_sprites_group.update()
        scoreboard.update()
        dinosaur.update()

        ground.draw(screen)
        cloud_sprites_group.draw(screen)
        ptera_sprites_group.draw(screen)
        cactus_sprites_group.draw(screen)
        scoreboard.draw(screen)
        dinosaur.draw(screen)

        pygame.display.update()
        clock.tick(FPS)

        for _ in ptera_sprites_group:
            if pygame.sprite.collide_mask(dinosaur, _):
                dinosaur.die()
                dinosaur.update()
                pygame.display.update()
                process = 'end'
                break

        for _ in cactus_sprites_group:
            if pygame.sprite.collide_mask(dinosaur, _):
                dinosaur.die()
                dinosaur.update()
                pygame.display.update()
                process = 'end'
                break

        while process == "end":

            screen.fill(BACKGROUND_COLOR)

            restart.update()

            ground.draw(screen)
            cloud_sprites_group.draw(screen)
            ptera_sprites_group.draw(screen)
            cactus_sprites_group.draw(screen)
            scoreboard.draw(screen)
            dinosaur.draw(screen)
            restart.draw(screen)
            game_over.draw(screen)

            pygame.display.update()
            clock.tick(FPS)

            with open('data/high_score.py', 'w') as f:
                if scoreboard.high_score < scoreboard.score:
                    f.write(str(scoreboard.score))
                else:
                    f.write(str(scoreboard.high_score))

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    repeat = False
                    pygame.quit()
                    sys.exit()

                key_list = pygame.key.get_pressed()

                if event.type == pygame.MOUSEBUTTONDOWN or key_list[pygame.K_SPACE] or key_list[pygame.K_UP]:
                    del game_over
                    del restart
                    image_restart = list()
                    for i in range(1, 9):
                        image_restart.append(pygame.image.load(IMAGE_PATHS['restart{}'.format(i)]))
                    restart = Pause(image_restart, (350, 150))

                    game_over_image = pygame.image.load(IMAGE_PATHS['game_over'])
                    game_over = GameOver(game_over_image)

                    ground.distance = 0
                    refresh_obstacle_count = 0
                    scoreboard.score = 0

                    for i in cactus_sprites_group:
                        i.kill()

                    for i in ptera_sprites_group:
                        i.kill()

                    for i in cloud_sprites_group:
                        i.kill()

                    dinosaur.state = "run"
                    dinosaur.rect.bottom = SCREENSIZE[1] - 11

                    process = "start"
