import pygame

from bullet import Bullet

class Hero():
    def __init__(self, settings, screen, bullets):
        self.settings = settings
        """
        hero对象里包含它发出的所有子弹的集合的引用self.bullets
        """
        self.bullets = bullets
        self.screen = screen

        self.screen_rect = screen.get_rect()
        self.image = pygame.image.load("../images/hero.gif")
        self.rect = self.image.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.centerx = float(self.rect.centerx)

        self.moving_left = False
        self.moving_right = False
        self.isfire = False
        self.fire_counter = 0       # 记录按下空格开火的时间
        self.is_hit = False

        self.blowup_image = [pygame.image.load("../images/hero_blowup_n" + str(i) + ".png") for i in range(1, 5)]
        self.blowup_index = 0
        self.blowup_interval = settings.hero_blowup_interval

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.settings.hero_speed
        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.settings.hero_speed
        self.rect.centerx = self.centerx

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        """
        按下空格键开火，松开空格键，停火
        按下空格键，发出第一发子弹，然后每循环100次发出一颗子弹
        松开空格键，把循环次数清0，以便下次按下空格键能立即发出第一颗子弹
        """
        if self.isfire:
            self.fire()

    def fire(self):
        if ((self.settings.counter - self.fire_counter) % self.settings.bullet_interval) == 0:
            self.bullets.add(Bullet(self.settings, self.screen, self.rect))

    def blitme(self):
        self.screen.blit(self.image, self.rect)
    
    def blowup(self):
        self.screen.blit(self.blowup_image[self.blowup_index], self.rect)

    def flicker(self):
        if self.blowup_index % 2 == 0:
            self.blitme()
