import pygame
from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, FONT_STYLE, FONT_SIZE, WHITE, BLACK, MENU3, GAMEOVER

class GameOverMenu:
    def __init__(self, score, max_score, enemies_eliminated):
        self.score = score
        self.max_score = max_score
        self.enemies_eliminated = enemies_eliminated
        self.font = pygame.font.SysFont(FONT_STYLE, FONT_SIZE)
        self.color = WHITE
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2
        self.background_image = MENU3
        self.game_over_image = GAMEOVER

    def draw(self, screen):
        screen.blit(self.background_image, (0, 0))
        screen.blit(self.game_over_image, (self.x - self.game_over_image.get_width() // 2, self.y - 200))

        score_text = self.font.render("Score: " + str(self.score), True, self.color)
        max_score_text = self.font.render("Max Score: " + str(self.max_score), True, self.color)
        enemies_text = self.font.render("Enemies Eliminated: " + str(self.enemies_eliminated), True, self.color)

        screen.blit(score_text, (self.x - score_text.get_width() // 2, self.y - 50))
        screen.blit(max_score_text, (self.x - max_score_text.get_width() // 2, self.y))
        screen.blit(enemies_text, (self.x - enemies_text.get_width() // 2, self.y + 50))

        pygame.draw.rect(screen, WHITE, (self.x - 75, self.y + 100, 150, 50))
        reset_text = self.font.render("Reset", True, BLACK)
        screen.blit(reset_text, (self.x - reset_text.get_width() // 2, self.y + 115))

        pygame.draw.rect(screen, WHITE, (self.x - 75, self.y + 175, 150, 50))
        exit_text = self.font.render("Exit", True, BLACK)
        screen.blit(exit_text, (self.x - exit_text.get_width() // 2, self.y + 190))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if self.x - 75 <= mouse_pos[0] <= self.x + 75:
                if self.y + 100 <= mouse_pos[1] <= self.y + 150:
                    return "reset"
                elif self.y + 175 <= mouse_pos[1] <= self.y + 225:
                    return "exit"
        return None

    def show_menu(self, screen):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    menu_option = self.handle_event(event)
                    if menu_option == "reset":
                        running = False

                    elif menu_option == "exit":
                        running = False
                        pygame.quit()
                        exit()

            screen.fill(BLACK)
            self.draw(screen)
            pygame.display.flip()

