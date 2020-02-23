import random

import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, settings, screen):
        super().__init__()
        self.settings = settings
        self.screen = screen
        
        self.screen_rect = screen.get_rect()
        self.image = pygame.image.load("../images/enemy0.png")
        self.rect = self.image.get_rect()

        self.rect.x = random.randrange(self.screen_rect.width - self.rect.width)
        self.rect.top = 0
        self.centerx = float(self.rect.centerx)
        self.y = float(self.rect.y)

        self.blowup_images = [pygame.image.load("../images/enemy0_down" + str(i) + ".png") for i in range(1, 5)]
        self.blowup_index = 0
        self.blowup_interval = settings.enemy_blowup_interval

    def update(self):
        self.y += self.settings.enemy_speed
        self.rect.y = self.y

    def blowup(self):
        self.screen.blit(self.blowup_images[self.blowup_index], self.rect)

#    def blitme(self):
#        self.screen.blit(self.image, self.rect)