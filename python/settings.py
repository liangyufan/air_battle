import pygame

class Settings:
    def __init__(self):
        self.counter = 0
        self.max_count = 1000
        # hero
        self.hero_speed = 1
        self.hero_blowup_interval = 30
        # hero bullet
        self.bullet_interval = 100
        self.bullet_speed = 1
        # enemy
        self.enemy_interval = 500
        self.enemy_speed = 0.3
        self.enemy_blowup_interval = 10
        # enemy bullet
        self.enemy_bullet_interval = 500
        self.enemy_bullet_speed = 0.5