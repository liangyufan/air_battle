import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, settings, screen, hero_rect):
        super().__init__()
        self.settings = settings
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.image = pygame.image.load("../images/bullet-1.gif")
        self.rect = self.image.get_rect()
        self.rect.centerx = hero_rect.centerx
        self.rect.bottom = hero_rect.top

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

#    def blitme(self):
#        self.screen.blit(self.image, self.rect)