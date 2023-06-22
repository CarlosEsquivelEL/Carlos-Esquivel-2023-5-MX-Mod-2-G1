import pygame
from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
from game.utils.constants import BLACK
from game.components.spaceship import Spaceship
from game.components.enemy import Enemy


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 10 # el numero de pixeles que el "objeto / imagen" se mueve en patalla
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.spaceship = Spaceship()
        self.enemies = []

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
        else:
            print("Something ocurred to quit the game!")
        pygame.display.quit()
        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def reset_game(self):
        self.spaceship.reset()
        self.enemy_handler.reset()
        self.score.reset()
        self.game_over = False
        self.game_over_menu = None

    def update(self, delta_time):
        events = pygame.key.get_pressed()
        self.spaceship.update(events)
        
        for enemy in self.enemies:
            enemy.update()

        if len(self.enemies) == 0:
            self.regenerate_enemies()

    def draw(self):
        self.clock.tick(FPS) # configuro cuantos frames per second voy a dibujar
        self.screen.fill((255, 255, 255)) # lleno el screen de color BLANCO???? 255, 255, 255 es el codigo RGB
        self.draw_background()
        self.spaceship.draw(self.screen)
        self.enemy_handler.draw(self.screen)
        self.power_handler.draw(self.screen)
        self.score.draw(self.screen)

        if self.game_over:
            if self.game_over_menu is None:
                self.game_over_menu = GameOverMenu(self.score.value, self.score.max_score, self.score.enemies_eliminated)
            self.game_over_menu.draw(self.screen)

        pygame.display.update() # esto hace que el dibujo se actualice en el display de pygame
        pygame.display.flip()  # hace el cambio

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))

    def update_background(self):
        self.y_pos_bg += self.game_speed
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed

    def regenerate_enemies(self):
        for _ in range(10):
            enemy = Enemy()
            enemy.rect.x = random.randint(0, SCREEN_WIDTH - enemy.rect.width)
            enemy.rect.y = random.randint(-enemy.rect.height, -10)
            self.enemies.append(enemy)

