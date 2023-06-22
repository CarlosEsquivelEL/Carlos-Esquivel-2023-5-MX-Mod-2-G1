import pygame
from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
from game.utils.constants import BLACK
from game.components.spaceship import Spaceship
from game.components.enemigos.enemy_handler import EnemyHandler
from game.components.collision import CollisionHandler
from game.components.score import Score
from game.components.powers.power_handler import PowerHandler
from game.components.menus.game_over import GameOverMenu
from game.components.menus.menu_main import MainMenu
from game.components.menus.menu_pause import PauseMenu

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
        self.score = Score()
        self.power_handler = PowerHandler()
        self.game_over_menu = None
        self.game_over = False 
        self.main_menu = MainMenu(self)
        self.pause_menu = PauseMenu(self)

    def run(self):
        self.main_menu.main_loop()

    def start_game(self):
        self.playing = True
        while self.playing:
            delta_time = self.clock.tick(FPS)
            self.handle_events()
            if not self.game_over and not self.paused:
                self.update(delta_time)
            self.draw()
            pygame.display.update()

        pygame.display.quit()
        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
            elif self.game_over and self.game_over_menu is not None:
                menu_action = self.game_over_menu.handle_event(event)
                if menu_action == "reset":
                    self.reset_game()
                elif menu_action == "exit":
                    self.playing = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if not self.paused:
                        self.pause_game()
                    else:
                        self.resume_game()

    def reset_game(self):
        self.spaceship.reset()
        self.enemy_handler.reset()
        self.score.reset()
        self.game_over = False
        self.game_over_menu = None

    def update(self, delta_time):
        events = pygame.key.get_pressed()
        self.spaceship.update(events)
        self.enemy_handler.update()
        self.enemy_handler.shoot_bullets()
        self.spaceship.update_bullets()
        self.power_handler.update(delta_time, self.spaceship, self.enemy_handler)
        self.collision_handler.handle_collisions(self)
        if not self.spaceship.is_alive:
            self.game_over = True 
        self.update_background()

    def draw(self):
        self.screen.fill(BLACK)
        self.draw_background()
        self.spaceship.draw(self.screen)
        self.enemy_handler.draw(self.screen)
        self.power_handler.draw(self.screen)
        self.score.draw(self.screen)

        if self.game_over:
            if self.game_over_menu is None:
                self.game_over_menu = GameOverMenu(self.score.value, self.score.max_score, self.score.enemies_eliminated)
            self.game_over_menu.draw(self.screen)

        if self.paused:
            self.pause_menu.draw_menu()

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))

    def update_background(self):
        self.y_pos_bg += self.game_speed
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.y_pos_bg = 0

    def pause_game(self):
        self.paused = True
        pause_menu = PauseMenu(self)
        pause_menu.main_loop()

    def resume_game(self):
        self.paused = False

    
    
