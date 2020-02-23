import pygame

class EnemyBullet(pygame.sprite.Sprite):
    def __init__(self, settings, screen, enemy):
        super().__init__()
        self.settings = settings
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.image = pygame.image.load("../images/bullet.png")
        self.rect = self.image.get_rect()
        self.rect.center = enemy.rect.center
        self.rect.y = enemy.rect.bottom
        self.y = float(self.rect.y)

    def update(self):
        self.y += self.settings.enemy_bullet_speed
        self.rect.y = self.y