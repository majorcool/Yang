import pygame


class Dinosaur(pygame.sprite.Sprite):

    def __init__(self, images_day, images_night, position):
        pygame.sprite.Sprite.__init__(self)
        self.images = images_day
        self.images_day = images_day
        self.images_night = images_night
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.bottom = position
        self.state = "begin"
        self.mask = pygame.mask.from_surface(self.image)
        self.refresh_counter = 0
        self.refresh_rate = 10
        self.up_speed = 0
        self.a = 0.8
        self.end_position = self.rect.bottom
        self.mask = pygame.mask.from_surface(self.image)
        self.fist_up_speed = 0

    def jump(self, up_speed):
        self.state = "jump"
        self.image = self.images[6]
        pygame.mixer.Sound('C:/Users/86153/Desktop/校企联培/作业/PA3/audios/jump.mp3').play()
        self.fist_up_speed = self.up_speed = up_speed  # 负数
        self.end_position = self.rect.bottom

    def duck(self):
        self.state = "duck"
        self.rect.bottom = self.end_position
        if self.image == self.images[0]:
            self.image = self.images[5]
        else:
            self.image = self.images[4]
        self.mask = pygame.mask.from_surface(self.image)

    def unduck(self):
        self.state = 'unduck'
        if self.image == self.images[5]:
            self.image = self.images[0]
        else:
            self.image = self.images[1]
        self.mask = pygame.mask.from_surface(self.image)
        self.state = "run"

    def die(self):
        self.state = "died"
        pygame.mixer.Sound('C:/Users/86153/Desktop/校企联培/作业/PA3/audios/die.mp3').play()

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        self.mask = pygame.mask.from_surface(self.image)

    def refresh_duck(self):
        if self.image == self.images[5]:
            self.image = self.images[4]
        else:
            self.image = self.images[5]
        self.mask = pygame.mask.from_surface(self.image)

    def refresh(self):
        if self.image == self.images[0]:
            self.rect.left -= 1
            self.image = self.images[1]
        else:
            self.rect.left += 1
            self.image = self.images[0]
        self.mask = pygame.mask.from_surface(self.image)

    def start(self):
        self.image = self.images[7]

    def update(self, mode):
        if mode == 0:
            self.images = self.images_day
        else:
            self.images = self.images_night

        if self.state == "run":
            if self.refresh_counter == self.refresh_rate:
                self.refresh()
                self.refresh_counter = 0
            self.refresh_counter += 1

        if self.state == "jump":
            self.rect.top += self.up_speed
            self.up_speed += self.a
            if self.rect.bottom >= self.end_position:
                self.rect.bottom = self.end_position
                self.up_speed = 0
                self.state = "run"

        if self.state == "died":
            self.image = self.images[2]

        if self.state == "duck":
            if self.refresh_counter == self.refresh_rate:
                self.refresh_duck()
                self.refresh_counter = 0
            self.refresh_counter += 1

