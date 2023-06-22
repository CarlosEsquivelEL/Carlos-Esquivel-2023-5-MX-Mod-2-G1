import pygame
from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE
from game.utils.constants import BLACK
from game.components.spaceship import Spaceship
from game.components.enemigos.enemy_handler import EnemyHandler
from game.components.collision import CollisionHandler
from game.components.score.score import Score
from game.components.powers.power_handler import PowerHandler

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.paused = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.spaceship = Spaceship()
        self.enemy_handler = EnemyHandler()
        self.collision_handler = CollisionHandler()
        self.score = Score(self.enemy_handler)
        self.power_handler = PowerHandler()

    def run(self):
        self.playing = True
        while self.playing:
            delta_time = self.clock.tick(FPS)
            self.handle_events()
            self.update(delta_time)
            self.draw()
            self.y_pos_bg += self.game_speed  # Actualizar la posición y del fondo
        else:
            print("Something occurred to quit the game!")
        pygame.display.quit()
        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self, delta_time):
        events = pygame.key.get_pressed()
        self.spaceship.update(events)
        self.enemy_handler.update()
        self.enemy_handler.shoot_bullets()
        self.spaceship.update_bullets()
        self.power_handler.update(delta_time, self.spaceship, self.enemy_handler)
        self.collision_handler.handle_collisions(self)

    def draw(self):
        self.screen.fill(BLACK)
        self.draw_background()
        self.spaceship.draw(self.screen)
        self.enemy_handler.draw(self.screen)
        self.power_handler.draw(self.screen)
        self.score.draw(self.screen)
        pygame.display.update()

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.y_pos_bg = 0  # Reiniciar la posición y del fondo si se sale de la pantalla
