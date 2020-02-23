import sys
import pygame

from settings import Settings
from hero import Hero
from bullet import Bullet
from enemy import Enemy
from enemy_bullet import EnemyBullet

def __keydown_handler(event, settings, hero):
    if event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_RIGHT:
        hero.moving_right = True
    elif event.key == pygame.K_LEFT:
        hero.moving_left = True
    elif event.key == pygame.K_SPACE:
        hero.isfire = True
        hero.fire_counter = settings.counter

def __keyup_handler(event, hero):
    if event.key == pygame.K_RIGHT:
        hero.moving_right = False
    elif event.key == pygame.K_LEFT:
        hero.moving_left = False
    elif event.key == pygame.K_SPACE:
        hero.isfire = False

def event_handler(settings, hero):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            __keydown_handler(event, settings, hero)
        elif event.type == pygame.KEYUP:
            __keyup_handler(event, hero)

def handle_enemies(settings, screen, enemies, enemy_bullets):
    if settings.counter % settings.enemy_interval == 0:
        enemies.add(Enemy(settings, screen))
    enemies.update()
    for enemy in enemies.copy():
        if settings.counter % settings.enemy_bullet_interval == 0:
            enemy_bullets.add(EnemyBullet(settings, screen, enemy))
        if enemy.rect.top > enemy.screen_rect.bottom:
            enemies.remove(enemy)
    enemy_bullets.update()
    for enemy_bullet in enemy_bullets.copy():
        if enemy_bullet.rect.top > enemy_bullet.screen_rect.bottom:
            enemy_bullets.remove(enemy_bullet)

def handle_hero_hit(hero, enemies, enemy_bullets):
    # by enemies or enemy_bullets
    enemy = pygame.sprite.spritecollideany(hero, enemies)
    enemy_bullet = pygame.sprite.spritecollideany(hero, enemy_bullets)
    if enemy:
        enemies.remove(enemy)
        hero.is_hit = True
    if enemy_bullet:
        enemy_bullets.remove(enemy_bullet)
        hero.is_hit = True

def handle_enemies_hit(bullets, enemies, enemies_blowup):
    # hero bullets hit the enemies
    dict = pygame.sprite.groupcollide(bullets, enemies, True, True)
    if dict:
        for enemys in dict.values():
            for enemy in enemys:
                enemies_blowup.add(enemy)

def screen_update(screen, background, hero, bullets, enemies, enemy_bullets, enemies_blowup):
    screen.blit(background, (0, 0))
    if hero.is_hit:
        if hero.blowup_index < 4:
            hero.blowup()
        elif hero.blowup_index < 10:
            hero.flicker()
        else:
            hero.is_hit = False
            hero.blowup_index = 0

        if hero.blowup_interval == 0:
            hero.blowup_index += 1
            hero.blowup_interval = hero.settings.hero_blowup_interval
        else:
            hero.blowup_interval -= 1
    else:
        hero.blitme()
    enemies.draw(screen)
    for enemy in enemies_blowup.sprites():
        enemy.blowup()
        if enemy.blowup_interval == 0:
            enemy.blowup_index += 1
            if (enemy.blowup_index == 4):
                enemies_blowup.remove(enemy)
                continue
            enemy.blowup_interval = enemy.settings.enemy_blowup_interval
        else:
            enemy.blowup_interval -= 1
    bullets.draw(screen)
    enemy_bullets.draw(screen)
    pygame.display.flip()

def run_game():
    pygame.display.init()
    pygame.display.set_caption("Air Battle")
    screen = pygame.display.set_mode((480, 852))
    background = pygame.image.load("../images/background.png")

    settings = Settings()
    bullets = pygame.sprite.Group()
    hero = Hero(settings, screen, bullets)
    enemies = pygame.sprite.Group()
    enemy_bullets = pygame.sprite.Group()
    enemies_blowup = pygame.sprite.Group()

    while True:
        event_handler(settings, hero)

        hero.update()
        handle_enemies(settings, screen, enemies, enemy_bullets)
        bullets.update()
        enemy_bullets.update()
        handle_enemies_hit(bullets, enemies, enemies_blowup)
        if not hero.is_hit:
            # hero hit by enemies or enemy_bullets
            handle_hero_hit(hero, enemies, enemy_bullets)

        screen_update(screen, background, hero, bullets, enemies, enemy_bullets, enemies_blowup)
        settings.counter += 1
        if settings.counter == settings.max_count:
            settings.counter = 0

run_game()