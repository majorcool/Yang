import pygame


class Cactus(pygame.sprite.Sprite):

    def __init__(self, image, reverse_image, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.images_day = image
        self.images_night = reverse_image
        self.state = True
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.mask = pygame.mask.from_surface(self.image)

        self.speed = -6

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, mode):
        self.rect.left += self.speed
        if self.rect.right < 0:
            self.kill()

        if mode == 0:
            self.image = self.images_day
        else:
            self.image = self.images_night


class Ptera(pygame.sprite.Sprite):

    def __init__(self, image0, image1, image0_reverse, image1_reverse, position):
        pygame.sprite.Sprite.__init__(self)
        self.image_0 = image0
        self.image_1 = image1
        self.image_0_day = image0
        self.image_1_day = image1
        self.image_0_night = image0_reverse
        self.image_1_night = image1_reverse
        self.image = self.image_0
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.mask = pygame.mask.from_surface(self.image)
        self.state = True

        self.speed = -6

        self.refresh_rate = 10
        self.refresh_counter = 0

    def refresh(self):
        if self.image == self.image_0:
            self.rect.top -= 14
            self.rect.left += 5
            self.image = self.image_1
        else:
            self.rect.top += 14
            self.rect.left -= 5
            self.image = self.image_0
        self.mask = pygame.mask.from_surface(self.image)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, mode):
        if self.refresh_counter == self.refresh_rate:
            self.refresh()
            self.refresh_counter = 0
        self.refresh_counter += 1

        self.rect.left += self.speed
        if self.rect.right < 0:
            self.state = False
            self.kill()

        if mode == 0:
            self.image_0 = self.image_0_day
            self.image_1 = self.image_1_day
        else:
            self.image_0 = self.image_0_night
            self.image_1 = self.image_1_night


