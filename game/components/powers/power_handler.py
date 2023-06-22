import random
import pygame
from game.components.powers.power1_2 import Life, Shield
from game.utils.constants import SCREEN_WIDTH, HEART

class PowerHandler:
    def __init__(self):
        self.lifes = []
        self.shields = []
        self.spawn_timer = 0
        self.spawn_interval = 5000
        self.shield_duration = 10000  # Duración del escudo en milisegundos
        self.shield_timer = 0

    def update(self, delta_time, spaceship, enemy_handler):
        self.spawn_timer += delta_time
        if self.spawn_timer >= self.spawn_interval:
            self.spawn_timer = 0
            self.spawn_power()

        for life in self.lifes[:]:
            life.update()
            if life.rect.colliderect(spaceship.rect) and spaceship.is_alive and spaceship.life < 3:
                spaceship.increment_life()
                self.lifes.remove(life)
            elif life.rect.bottom < 0:
                self.lifes.remove(life)

        for shield in self.shields[:]:
            shield.update()
            if shield.rect.colliderect(spaceship.rect) and spaceship.is_alive and not spaceship.shield_active:
                spaceship.activate_shield()
                self.shields.remove(shield)
                self.shield_timer = pygame.time.get_ticks()
            elif shield.rect.bottom < 0:
                self.shields.remove(shield)

        if self.is_colliding_enemy(spaceship, enemy_handler):
            if not spaceship.shield_active:
                spaceship.decrement_life()
                if spaceship.life <= 0:
                    spaceship.is_alive = False

        if spaceship.shield_active and pygame.time.get_ticks() - self.shield_timer >= self.shield_duration:
            spaceship.deactivate_shield()

    def spawn_power(self):
        power_type = random.choice([Life, Shield])
        power = power_type()
        power.rect.x = random.randint(0, SCREEN_WIDTH - power.rect.width)
        power.rect.y = -power.rect.height  # Spawn item above the screen
        if isinstance(power, Life):
            self.lifes.append(power)
        elif isinstance(power, Shield):
            self.shields.append(power)

    def draw(self, screen):
        heart_image = HEART

        for life in self.lifes:
            screen.blit(heart_image, life.rect)

        for shield in self.shields:
            shield.draw(screen)

    def is_colliding_enemy(self, spaceship, enemy_handler):
        spaceship_rect = spaceship.rect

        for enemy in enemy_handler.enemies:
            enemy_rect = enemy.rect
            if spaceship_rect.colliderect(enemy_rect):
                return True

        for life in self.lifes:
            life_rect = life.rect
            if spaceship_rect.colliderect(life_rect) and spaceship.is_alive and spaceship.life < 3:
                return True

        for shield in self.shields:
            shield_rect = shield.rect
            if spaceship_rect.colliderect(shield_rect) and spaceship.is_alive and not spaceship.shield_active:
                return True

        return False
