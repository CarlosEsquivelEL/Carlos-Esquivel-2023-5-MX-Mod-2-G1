import pygame
from pygame.sprite import Sprite
from game.utils.constants import SPACESHIP, SPACESHIP_SHIELD
from game.utils.constants import SPACESHIP_SHIELD_WIDTH, SPACESHIP_SHIELD_HEIGHT
from game.components.bullets.bullet import Bullet_

class Spaceship(Sprite):
    def __init__(self):
        super().__init__()
        self.is_alive = True
        self.image_width = 40
        self.image_height = 60
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (self.image_width, self.image_height))
        self.rect = self.image.get_rect()
        self.screen = pygame.display.set_mode((1100, 600))
        self.reset_position()
        self.rect.x = 300
        self.rect.y = 500
        self.speed_x = 5
        self.speed_y = 5
        self.bullets = []
        self.bullet_speed = 10
        self.life = 3
        self.shield_active = False
        self.shield_image = pygame.transform.scale(SPACESHIP_SHIELD, (SPACESHIP_SHIELD_WIDTH, SPACESHIP_SHIELD_HEIGHT))

    def reset_position(self):
        self.rect.x = 300
        self.rect.y = 500
        
    def activate_shield(self):
        self.shield_active = True
        self.image = pygame.transform.scale(self.shield_image, (self.image_width, self.image_height))

    def deactivate_shield(self):
        self.shield_active = False
        self.image = pygame.transform.scale(SPACESHIP, (self.image_width, self.image_height))

    def decrement_life(self):
        self.life -= 1

    def restart_game(self):
        self.life = 3
        self.is_alive = True
        self.shield_active = False

    def update(self, events):
        if events[pygame.K_LEFT] and events[pygame.K_UP]:
            self.rect.x -= self.speed_x
            self.rect.y -= self.speed_y
        elif events[pygame.K_LEFT] and events[pygame.K_DOWN]:
            self.rect.x -= self.speed_x
            self.rect.y += self.speed_y
        elif events[pygame.K_RIGHT] and events[pygame.K_UP]:
            self.rect.x += self.speed_x
            self.rect.y -= self.speed_y
        elif events[pygame.K_RIGHT] and events[pygame.K_DOWN]:
            self.rect.x += self.speed_x
            self.rect.y += self.speed_y
        elif events[pygame.K_LEFT]:
            self.rect.x -= self.speed_x
        elif events[pygame.K_RIGHT]:
            self.rect.x += self.speed_x
        elif events[pygame.K_UP]:
            self.rect.y -= self.speed_y
        elif events[pygame.K_DOWN]:
            self.rect.y += self.speed_y
        elif events[pygame.K_SPACE]:
            self.shoot_bullets()

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        self.rect.clamp_ip(self.screen.get_rect())
        for bullet in self.bullets:
            bullet.draw(screen)

    def shoot_bullets(self):
        bullet = Bullet_()
        bullet.rect.centerx = self.rect.centerx
        bullet.rect.bottom = self.rect.centery
        self.bullets.append(bullet)

    def update_bullets(self):
        for bullet in self.bullets:
            bullet.update()

    def is_colliding_enemy(self):
        spaceship_rect = self.image.get_rect()
        for enemy in self.enemy_handler.enemies:
            enemy_rect = enemy.image.get_rect()
            if spaceship_rect.colliderect(enemy_rect):
                return True
        return False
    
    def reset(self):
        self.is_alive = True
        self.reset_position()
        self.bullets = []
        self.deactivate_shield()


