import pygame
import random
from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE
from game.components.spaceship import Spaceship
from game.components.enemy import Enemy
from game.components.bullet import Bullet

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.spaceship = Spaceship()
        self.enemies = []
        self.bullets = []

    def run(self):
        self.playing = True
        while self.playing:
            self.handle_events()
            self.update()
            self.draw()
        else:
            print("Something occurred to quit the game!")
        pygame.display.quit()
        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.spaceship.shoot()

    def update(self):
        events = pygame.key.get_pressed()
        self.spaceship.update(events)
        self.spaceship.update_bullets()

        for enemy in self.enemies:
            enemy.update()

            if self.spaceship.rect.colliderect(enemy.rect):
                print("Collision occurred!")
                self.playing = False

            for bullet in self.spaceship.bullets:
                if bullet.rect.colliderect(enemy.rect):
                    self.enemies.remove(enemy)
                    self.spaceship.bullets.remove(bullet)
                    break

        if len(self.enemies) == 0:
            self.regenerate_enemies()

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.spaceship.draw(self.screen)
        for enemy in self.enemies:
            enemy.draw(self.screen)

        for bullet in self.spaceship.bullets:
            bullet.draw(self.screen)

        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed

    def regenerate_enemies(self):
        for _ in range(10):
            enemy = Enemy()
            enemy.rect.x = random.randint(0, SCREEN_WIDTH - enemy.rect.width)
            enemy.rect.y = random.randint(-enemy.rect.height, -10)
            self.enemies.append(enemy)
