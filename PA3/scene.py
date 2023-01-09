import pygame


class Ground(pygame.sprite.Sprite):

    def __init__(self, image, position):
        pygame.sprite.Sprite.__init__(self)

        self.image_0 = image
        self.rect_0 = self.image_0.get_rect()
        self.rect_0.left, self.rect_0.bottom = position

        self.image_1 = image
        self.rect_1 = self.image_1.get_rect()
        self.rect_1.left, self.rect_1.bottom = self.rect_0.right, self.rect_0.bottom

        self.speed = -6
        self.distance = 0

    def draw(self, screen):
        screen.blit(self.image_0, self.rect_0)
        screen.blit(self.image_1, self.rect_1)

    def update(self):
        self.rect_0.left += self.speed
        self.rect_1.left += self.speed
        self.distance -= self.speed
        if self.rect_0.right < 0:
            self.rect_0.left = self.rect_1.right
            self.rect_1, self.rect_0 = self.rect_0, self.rect_1

    def distance_calculation(self):
        self.distance += 1


class Cloud(pygame.sprite.Sprite):

    def __init__(self, image, position):
        pygame.sprite.Sprite.__init__(self)

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.bottom = position

        self.speed = -3

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        self.rect.left += self.speed
        if self.rect.right <= 0:
            pygame.sprite.Sprite.kill(self)


class Moon(pygame.sprite.Sprite):

    def __init__(self, images, position):
        pygame.sprite.Sprite.__init__(self)
        self.images = images
        self.image_count = 0
        self.image = self.images[self.image_count]
        self.rect = self.image.get_rect()
        self.rect.top, self.rect.left = position

        self.speed = -4
        self.exist = True

    def update(self):
        self.rect.left += self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)
