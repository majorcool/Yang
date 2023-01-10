import time

import pygame


class Pause(pygame.sprite.Sprite):

    def __init__(self, images, images_reverse, position_first):
        pygame.sprite.Sprite.__init__(self)
        self.images = images
        self.images_day = images
        self.images_night = images_reverse
        self.image = self.images[0]
        self.small_rect = images[0].get_rect()
        self.small_rect.center = position_first
        self.rect = self.small_rect
        self.refresh_counter = 0
        self.refresh_rate = 20
        self.image_count = -1
        self.mask = pygame.mask.from_surface(self.image)
        self.background = (235, 235, 235)
        self.background_day = (235, 235, 235)
        self.background_night = (20, 20, 20)

    def refresh(self):
        self.image.fill(self.background)
        self.image_count += 1
        self.image_count = min(7, self.image_count)
        self.image = self.images[self.image_count]
        self.refresh_rate = 2
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.center = self.small_rect.center

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        if self.refresh_counter == self.refresh_rate:
            self.refresh()
            self.refresh_counter = 0
        self.refresh_counter += 1

    def judge(self, mode):
        if mode == 0:
            self.images = self.images_day
            self.background = self.background_day
        else:
            self.images = self.images_night
            self.background = self.background_night


class GameOver(pygame.sprite.Sprite):

    def __init__(self, image, image_reverse):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.image_day = image
        self.image_night = image_reverse
        self.rect = self.image_day.get_rect()
        self.rect.center = (350, 75)

    def update(self, mode):
        if mode == 0:
            self.image = self.image_day
        else:
            self.image = self.image_night

    def draw(self, screen):
        screen.blit(self.image, self.rect)


