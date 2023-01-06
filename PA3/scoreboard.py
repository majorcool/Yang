import pygame


class Scoreboard(pygame.sprite.Sprite):
    def __init__(self, images, position):
        pygame.sprite.Sprite.__init__(self)

        self.score = 0
        with open('data/high_score.py', 'r') as f:
            self.high_score = int(f.read().split('\n')[0])

        self.images = images
        self.image_score = self.rect_score = pygame.Surface((100, 31)).get_rect()
        self.image_high_score = self.rect_high_score = pygame.Surface((160, 31)).get_rect()
        self.rect_score.right, self.rect_score.top = position
        self.rect_high_score.right, self.rect_high_score.top = self.rect_score.left - 20, self.rect_score.top
        self.refresh_rate = 20
        self.refresh_rate_count = 3
        self.refresh_count = 0
        self.refresh_mode = 0
        self.remain_score = 0
        self.count = 0  # 解决一次刷新两个的bug

    def update(self):

        if self.score % 100 == 0 and self.score != 0:
            self.remain_score = self.score
            self.refresh_rate_count = 0
            self.refresh_mode = 0

        if self.refresh_rate_count < 3:
            self.refresh_count += 1
            self.refresh()
            self.rect_score.right, self.rect_score.top = 700, 0

        if self.refresh_rate_count < 3 and self.refresh_count == self.refresh_rate:
            self.refresh_rate_count += 1
            self.refresh_count = 0
            if self.refresh_mode == 0:
                self.refresh_mode = 1
            else:
                self.refresh_mode = 0

        if self.refresh_rate_count >= 3:
            self.image_score = pygame.Surface((100, 31))
            self.image_score.fill((235, 235, 235))
            score = str(self.score).zfill(5)
            for i in range(0, len(score)):
                self.image_score.blit(self.images[int(score[i])], (20 * i, 0))

        self.image_high_score = pygame.Surface((160, 31))
        self.image_high_score.set_alpha(215, 255)
        self.image_high_score.fill((235, 235, 235))
        self.image_high_score.blit(self.images[-1], (0, 0))
        for i, _ in enumerate(str(self.high_score).zfill(5)):
            self.image_high_score.blit(self.images[int(_)], (60 + 20 * i, 0))

    def draw(self, screen):
        screen.blit(self.image_score, self.rect_score)
        screen.blit(self.image_high_score, self.rect_high_score)

    def refresh(self):
        if self.refresh_mode == 0:
            self.image_score = pygame.Surface((100, 31))
            self.image_score.fill((235, 235, 235))
            self.image_score.set_alpha(0, 0)
            score = str(self.remain_score).zfill(5)
            for i in range(0, len(score)):
                self.image_score.blit(self.images[int(score[i])], (20 * i, 0))
        else:
            self.image_score = pygame.Surface((100, 31))
            self.image_score.fill((235, 235, 235))
            score = str(self.remain_score).zfill(5)
            for i in range(0, len(score)):
                self.image_score.blit(self.images[int(score[i])], (20 * i, 0))
            self.rect_score = self.image_score.get_rect()


