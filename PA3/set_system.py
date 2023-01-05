import time

import pygame


class Pause(pygame.sprite.Sprite):

    def __init__(self, images, position_first):
        pygame.sprite.Sprite.__init__(self)
        self.images = images
        self.image = self.images[0]
        self.small_rect = images[0].get_rect()
        self.small_rect.center = position_first
        self.rect = self.small_rect
        self.refresh_counter = 0
        self.refresh_rate = 20
        self.image_count = -1
        self.mask = pygame.mask.from_surface(self.image)

    def refresh(self):
        self.image_count = min(6, self.image_count)
        self.image_count += 1
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


class GameOver(pygame.sprite.Sprite):

    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (350, 75)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

