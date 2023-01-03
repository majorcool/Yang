import pygame


class Scoreboard(pygame.sprite.Sprite):
    def __init__(self, images, position):
        pygame.sprite.Sprite.__init__(self)

        self.score = 99
        with open('data/high_score.py', 'r') as f:
            self.high_score = int(f.read().split('\n')[0])
        self.high_score_digits = max(5, len(str(self.high_score)))

        self.images = images
        self.image_score = self.rect_score = self.images[0].get_rect()
        self.image_high_score = self.rect_high_score = self.images[0].get_rect()
        self.rect_score.right, self.rect_score.top = position
        self.rect_high_score.right, self.rect_high_score.top = self.rect_score.left - 20, self.rect_score.top

    def update(self):
        self.image_score = pygame.Surface((100, 31))
        self.image_score.fill((235, 235, 235))
        for i, _ in enumerate(str(self.score).zfill(5)):
            self.image_score.blit(self.images[int(_)], (20 * i, 0))

        self.image_high_score = pygame.Surface((160, 31))
        self.image_high_score.fill((235, 235, 235))
        self.image_high_score.blit(self.images[-1], (0, 0))
        for i, _ in enumerate(str(self.high_score).zfill(self.high_score_digits)):
            self.image_high_score.blit(self.images[int(_)], (60 + 20 * i, 0))

    def draw(self, screen):
        screen.blit(self.image_score, self.rect_score)
        screen.blit(self.image_high_score, self.rect_high_score)
