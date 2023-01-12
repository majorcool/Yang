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
from scene import Moon
from scene import Stars


def reverse_color(image):  # 夜间模式反色处理
    image_reverse = image.copy()
    width, height = image_reverse.get_size()
    for pos in [(x, y) for x in range(width) for y in range(height)]:
        color = image_reverse.get_at(pos)
        if color.a != 0:
            color = ~color
            color.a = 255
            image_reverse.set_at(pos, color)
    return image_reverse


#  循环变量
FPS = 60
TITLE = 'Chrome Dino'
BACKGROUND_COLOR = (235, 235, 235)
SCREENSIZE = (700, 300)
pygame.init()
screen = pygame.display.set_mode(SCREENSIZE)
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()
pygame.key.set_repeat(50)
IMAGE_PATHS = {
    'ground': 'C:/Users/86153/Desktop/校企联培/作业/PA3/images/ground.png',
    'cloud': 'C:/Users/86153/Desktop/校企联培/作业/PA3/images/cloud.png',
    'ptera1': 'C:/Users/86153/Desktop/校企联培/作业/PA3/images/pterodactyl-1.png',
    'ptera2': 'C:/Users/86153/Desktop/校企联培/作业/PA3/images/pterodactyl-2.png',
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
    'dinosaur0': 'C:/Users/86153/Desktop/校企联培/作业/PA3/images/dinosaur-run-1.png',
    'dinosaur1': 'C:/Users/86153/Desktop/校企联培/作业/PA3/images/dinosaur-run-2.png',
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
    'game_over': 'C:/Users/86153/Desktop/校企联培/作业/PA3/images/game-over.png',
    'moon1': 'C:/Users/86153/Desktop/校企联培/作业/PA3/images/moon-1.png',
    'moon2': 'C:/Users/86153/Desktop/校企联培/作业/PA3/images/moon-2.png',
    'moon3': 'C:/Users/86153/Desktop/校企联培/作业/PA3/images/moon-3.png',
    'moon4': 'C:/Users/86153/Desktop/校企联培/作业/PA3/images/moon-4.png',
    'moon5': 'C:/Users/86153/Desktop/校企联培/作业/PA3/images/moon-5.png',
    'moon6': 'C:/Users/86153/Desktop/校企联培/作业/PA3/images/moon-6.png',
    'moon7': 'C:/Users/86153/Desktop/校企联培/作业/PA3/images/moon-7.png',
    'star1': 'C:/Users/86153/Desktop/校企联培/作业/PA3/images/star-1.png',
    'star2': 'C:/Users/86153/Desktop/校企联培/作业/PA3/images/star-2.png',
    'star3': 'C:/Users/86153/Desktop/校企联培/作业/PA3/images/star-3.png',
}


#  图像载入和实例化
image_moon_1 = pygame.image.load(IMAGE_PATHS['moon1'])
image_moon_2 = pygame.image.load(IMAGE_PATHS['moon2'])
image_moon_3 = pygame.image.load(IMAGE_PATHS['moon3'])
image_moon_4 = pygame.image.load(IMAGE_PATHS['moon4'])
image_moon_5 = pygame.image.load(IMAGE_PATHS['moon5'])
image_moon_6 = pygame.image.load(IMAGE_PATHS['moon6'])
image_moon_7 = pygame.image.load(IMAGE_PATHS['moon7'])
image_moon_list = list()
image_moon_list.append(image_moon_1)
image_moon_list.append(image_moon_2)
image_moon_list.append(image_moon_3)
image_moon_list.append(image_moon_4)
image_moon_list.append(image_moon_5)
image_moon_list.append(image_moon_6)
image_moon_list.append(image_moon_7)
moon = Moon(image_moon_list, (random.randint(0, 700), 50))

image_star_1 = pygame.image.load(IMAGE_PATHS['star1'])
image_star_2 = pygame.image.load(IMAGE_PATHS['star2'])
image_star_3 = pygame.image.load(IMAGE_PATHS['star3'])
stars_sprites_group = pygame.sprite.Group()

image_ground = pygame.image.load(IMAGE_PATHS['ground'])
image_ground_reverse = reverse_color(image_ground)
ground = Ground(image_ground, image_ground_reverse, (0, SCREENSIZE[1]))

image_cloud = pygame.image.load(IMAGE_PATHS['cloud'])
image_cloud_reverse = reverse_color(image_cloud)
cloud_sprites_group = pygame.sprite.Group()

image_ptera_0 = pygame.image.load(IMAGE_PATHS['ptera1'])
image_ptera_1 = pygame.image.load(IMAGE_PATHS['ptera2'])
ptera_sprites_group = pygame.sprite.Group()
image_ptera_0_reverse = reverse_color(image_ptera_0)
image_ptera_1_reverse = reverse_color(image_ptera_1)

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
image_dinosaur_reverse = list()
image_dinosaur_reverse.append(reverse_color(image_dinosaur_0))
image_dinosaur_reverse.append(reverse_color(image_dinosaur_1))
image_dinosaur_reverse.append(reverse_color(image_dinosaur_2))
image_dinosaur_reverse.append(reverse_color(image_dinosaur_3))
image_dinosaur_reverse.append(reverse_color(image_dinosaur_4))
image_dinosaur_reverse.append(reverse_color(image_dinosaur_5))
image_dinosaur_reverse.append(reverse_color(image_dinosaur_6))
image_dinosaur_reverse.append(reverse_color(image_dinosaur_7))
dinosaur = Dinosaur(image_dinosaur, image_dinosaur_reverse, (0, SCREENSIZE[1]-11))

image_cactus_1 = pygame.image.load(IMAGE_PATHS['cactus1'])
image_cactus_2 = pygame.image.load(IMAGE_PATHS['cactus2'])
image_cactus_3 = pygame.image.load(IMAGE_PATHS['cactus3'])
image_cactus_4 = pygame.image.load(IMAGE_PATHS['cactus4'])
image_cactus_5 = pygame.image.load(IMAGE_PATHS['cactus5'])
image_cactus_6 = pygame.image.load(IMAGE_PATHS['cactus6'])
cactus_sprites_group = pygame.sprite.Group()
image_cactus_1_reverse = reverse_color(image_cactus_1)
image_cactus_2_reverse = reverse_color(image_cactus_2)
image_cactus_3_reverse = reverse_color(image_cactus_3)
image_cactus_4_reverse = reverse_color(image_cactus_4)
image_cactus_5_reverse = reverse_color(image_cactus_5)
image_cactus_6_reverse = reverse_color(image_cactus_6)

image_scoreboard = list()
for i in range(0, 11):
    image_scoreboard.append(pygame.image.load(IMAGE_PATHS[str(i)]))
image_scoreboard_reverse = list()
for i in range(0, 11):
    image_scoreboard_reverse.append(reverse_color(pygame.image.load(IMAGE_PATHS[str(i)])))
scoreboard = Scoreboard(image_scoreboard, image_scoreboard_reverse, (SCREENSIZE[0], 0))

image_restart = list()
for i in range(1, 9):
    image_restart.append(pygame.image.load(IMAGE_PATHS['restart{}'.format(i)]))
image_restart_reverse = list()
for i in range(1, 9):
    image_restart_reverse.append(reverse_color(pygame.image.load(IMAGE_PATHS['restart{}'.format(i)])))
restart = Pause(image_restart, image_restart_reverse, (350, 150))

game_over_image = pygame.image.load(IMAGE_PATHS['game_over'])
game_over_image_reverse = reverse_color(game_over_image)
game_over = GameOver(game_over_image, game_over_image_reverse)


#  循环判断变量
process = 'begin'
refresh_obstacle = 50
refresh_obstacle_count = 0
refresh_cloud = 50
refresh_cloud_count = 0
refresh_stars = 50
refresh_stars_count = 0
up_speed = -6
broadcasting = None
prepare_jump = False
repeat = True
difficult = 0
scene_mode = 0  # 0代表白天，1代表黑夜
scene_time_day = 200
scene_time_night = 1000
scene_time_count = 0
scene_time = scene_time_day


#  开始界面，不参与大循环，只执行一次
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


#  游戏中和结束的循环
while repeat:

    if process == 'start':
        scene_time_count = 0
        scene_mode = 0
        moon.image_count = -1

    while process == 'start':

        #  键盘捕捉
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

            if event.type == pygame.KEYDOWN:

                #  根据按键盘时间增加初速度，根据vf=vi+gt进行计算每帧的下落速度，再将下落速度与距离相加
                if (event.key == pygame.K_UP or event.key == pygame.K_SPACE) and (dinosaur.state == "run" or dinosaur.state == "jump"):
                    up_speed -= 2
                    up_speed = max(-20, up_speed)
                    broadcasting = "jump"
                    prepare_jump = True

                if event.key == pygame.K_DOWN and (dinosaur.state == "jump" or dinosaur.state == "run"):
                    if dinosaur.state == "jump":
                        dinosaur.up_speed = 30
                    if dinosaur.end_position - dinosaur.rect.bottom <= 30:  # 直接进行判断，避免重复循环，可减小1帧的时间误差
                        dinosaur.duck()

            elif event.type == pygame.KEYUP:

                if broadcasting == "jump" and prepare_jump and not dinosaur.state == "jump":
                    dinosaur.jump(up_speed)
                    up_speed = -10
                    prepare_jump = False

                if dinosaur.state == "duck" and not key_list[pygame.K_DOWN]:
                    dinosaur.unduck()

        #  scoreboard计分
        scoreboard.score = ground.distance//50
        if scoreboard.score and not scoreboard.score % 100:
            pygame.mixer.Sound('C:/Users/86153/Desktop/校企联培/作业/PA3/audios/score.mp3').play()

        #  难度调试
        difficult = min(4, ground.distance//10000)  # 200切难度
        if difficult == 0:
            dinosaur.a = 0.8
            ground.speed = -6
            ptera_sprites_group.speed = -6
            cactus_sprites_group.speed = -6
            refresh_obstacle = 70
        elif difficult == 1:
            dinosaur.a = 0.85
            ground.speed = -7
            ptera_sprites_group.speed = -7
            cactus_sprites_group.speed = -7
            refresh_obstacle = 65
        elif difficult == 2:
            dinosaur.a = 0.9
            ground.speed = -8
            ptera_sprites_group.speed = -8
            cactus_sprites_group.speed = -8
            refresh_obstacle = 60
        elif difficult == 3:
            dinosaur.a = 0.95
            ground.speed = -9
            ptera_sprites_group.speed = -9
            cactus_sprites_group.speed = -9
            refresh_obstacle = 55
        elif difficult == 4:
            dinosaur.a = 1
            ground.speed = -10
            ptera_sprites_group.speed = -10
            cactus_sprites_group.speed = -10
            refresh_obstacle = 50

        #  实例化和刷新部分精灵
        if len(cloud_sprites_group) < 5 and refresh_cloud_count >= refresh_cloud:
            generate = random.randint(1, 100)
            if generate == 1:
                cloud_sprites_group.add(Cloud(image_cloud, image_cloud_reverse, (SCREENSIZE[0], random.randint(30, 75))))
                refresh_cloud_count = 0
        refresh_cloud_count += 1

        if len(cloud_sprites_group) < 1:
            cloud_sprites_group.add(Cloud(image_cloud, image_cloud_reverse, (SCREENSIZE[0], random.randint(30, 75))))

        for cloud in cloud_sprites_group:
            if cloud.rect.right <= 0:
                cloud_sprites_group.remove(cloud)

        if len(ptera_sprites_group) < 5 and refresh_obstacle_count >= refresh_obstacle:
            generate = random.randint(1, 100)
            if generate == 6:
                ptera_sprites_group.add(
                    Ptera(image_ptera_0, image_ptera_1, image_ptera_0_reverse, image_ptera_1_reverse, (SCREENSIZE[0], random.randint(120, 235))))
                refresh_obstacle_count = 0

        if len(cactus_sprites_group) < 5 and refresh_obstacle_count >= refresh_obstacle:
            generate = random.randint(1, 50)
            if generate == 6:
                magnitude = random.choice((image_cactus_1, image_cactus_2, image_cactus_3, image_cactus_4,
                                           image_cactus_5, image_cactus_6))
                refresh_obstacle_count = 0
                if magnitude == image_cactus_1:
                    cactus_sprites_group.add(Cactus(magnitude, reverse_color(magnitude), (SCREENSIZE[0], 193)))
                if magnitude in (image_cactus_2, image_cactus_3):
                    cactus_sprites_group.add(Cactus(magnitude, reverse_color(magnitude), (SCREENSIZE[0], 195)))
                if magnitude in (image_cactus_4, image_cactus_5, image_cactus_6):
                    cactus_sprites_group.add(Cactus(magnitude, reverse_color(magnitude), (SCREENSIZE[0], 220)))
        refresh_obstacle_count += 1

        for cactus in cactus_sprites_group:
            if cactus.rect.right <= 0:
                cactus_sprites_group.remove(cactus)

        #  夜间模式切换和基础背景设置
        if scene_mode == 0:
            scene_time = scene_time_day
            screen.fill(BACKGROUND_COLOR)
        else:
            scene_time = scene_time_night
            screen.fill((20, 20, 20))
            moon.update()

            if moon.rect.right <= 0:
                moon.rect.left = SCREENSIZE[0]
                moon.rect.top = 30

            if len(stars_sprites_group) < 5 and refresh_stars_count >= refresh_stars:
                generate = random.randint(1, 100)
                if generate == 1:
                    stars_sprites_group.add(
                        Stars(random.choice((image_star_1, image_star_2, image_star_3)), (SCREENSIZE[0], random.randint(30, 120))))
                    refresh_stars_count = 0
            refresh_stars_count += 1

            if len(stars_sprites_group) < 1:
                stars_sprites_group.add(
                    Stars(random.choice((image_star_1, image_star_2, image_star_3)), (SCREENSIZE[0], random.randint(30, 120))))

            for star in stars_sprites_group:
                if star.rect.right <= 0:
                    cloud_sprites_group.remove(star)

            stars_sprites_group.update()

            moon.draw(screen)
            stars_sprites_group.draw(screen)

        if scene_time <= scene_time_count and 1 == random.randint(1, 100):  # 刷新方式与障碍物一样，隔时间随机刷新
            if scene_mode == 0:
                scene_mode = 1

                moon.image_count = (moon.image_count + 1) % 7
                moon.renew()
                moon.rect.left = random.randint(0, 700)
                moon.rect.top = 30

                for i in stars_sprites_group:
                    i.rect.left = random.randint(0, 700)
                    i.rect.top = random.randint(30, 120)
                if len(stars_sprites_group) < 1:
                    stars_sprites_group.add(
                        Stars(random.choice((image_star_1, image_star_2, image_star_3)),
                              (random.randint(0, 700), random.randint(30, 120))))

            else:
                scene_mode = 0

                moon.rect.right = -100  # 将月亮和星星移到图外
                for star in stars_sprites_group:
                    star.rect.right = -100

            scene_time_count = 0

        scene_time_count += 1

        # 刷新精灵
        ground.update(scene_mode)
        cloud_sprites_group.update(scene_mode)
        ptera_sprites_group.update(scene_mode)
        cactus_sprites_group.update(scene_mode)
        scoreboard.update(scene_mode)
        dinosaur.update(scene_mode)

        ground.draw(screen)
        cloud_sprites_group.draw(screen)
        ptera_sprites_group.draw(screen)
        cactus_sprites_group.draw(screen)
        scoreboard.draw(screen)
        dinosaur.draw(screen)

        pygame.display.update()
        clock.tick(FPS)

        # 碰撞检测
        for _ in ptera_sprites_group:
            if pygame.sprite.collide_mask(dinosaur, _):
                dinosaur.die()
                dinosaur.update(scene_mode)
                game_over.update(scene_mode)
                restart.judge(scene_mode)
                pygame.display.update()
                if scene_mode == 0:
                    screen.fill(BACKGROUND_COLOR)
                else:
                    screen.fill((20, 20, 20))
                process = 'end'
                break

        for _ in cactus_sprites_group:
            if pygame.sprite.collide_mask(dinosaur, _):
                dinosaur.die()
                dinosaur.update(scene_mode)
                game_over.update(scene_mode)
                restart.judge(scene_mode)
                pygame.display.update()
                if scene_mode == 0:
                    screen.fill(BACKGROUND_COLOR)
                else:
                    screen.fill((20, 20, 20))
                process = 'end'
                break

        while process == "end":
            if restart.image_count < 7:
                restart.update()

            ground.draw(screen)
            cloud_sprites_group.draw(screen)
            ptera_sprites_group.draw(screen)
            cactus_sprites_group.draw(screen)
            scoreboard.draw(screen)
            dinosaur.draw(screen)
            restart.draw(screen)
            game_over.draw(screen)
            moon.draw(screen)

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
                    # 全部刷新
                    del game_over
                    del restart
                    image_restart = list()
                    for i in range(1, 9):
                        image_restart.append(pygame.image.load(IMAGE_PATHS['restart{}'.format(i)]))
                    restart = Pause(image_restart, image_restart_reverse, (350, 150))

                    game_over_image = pygame.image.load(IMAGE_PATHS['game_over'])
                    game_over = GameOver(game_over_image, game_over_image_reverse)

                    ground.distance = 0
                    refresh_obstacle_count = 0
                    scoreboard.score = 0
                    scene_time_count = 0
                    scene_mode = 0

                    for i in cactus_sprites_group:
                        i.kill()

                    for i in ptera_sprites_group:
                        i.kill()

                    for i in cloud_sprites_group:
                        i.kill()

                    dinosaur.state = "run"
                    dinosaur.rect.bottom = SCREENSIZE[1] - 11

                    process = "start"
