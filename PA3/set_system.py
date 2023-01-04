import time

import pygame


class Pause(pygame.sprite.Sprite):

    def __init__(self, images, position_first, position_second):
        pygame.sprite.Sprite.__init__(self)
        self.images = images
        self.image = self.images[0]
        self.small_rect = images[0].get_rect()
        self.big_rect = images[7].get_rect()
        self.small_rect.left, self.small_rect.top = position_first
        self.big_rect.left, self.big_rect.top = position_second

    def draw(self, screen):
        screen.blit(self.image, self.small_rect)
        time.sleep(1)
        for i in range(1, 3):
            self.image = self.images[i]
            screen.blit(self.image, self.small_rect)
        for i in range(3, 8):
            self.image = self.images[i]
            screen.blit(self.image, self.big_rect)
