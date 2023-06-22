import pygame
from game.utils.constants import BLACK
from game.components.menus.game_over import GameOverMenu

class CollisionHandler:
    def spaceship_enemy_collision(self, spaceship, enemy):
        return spaceship.rect.colliderect(enemy.rect)

    def bullet_enemy_collision(self, bullet, enemy):
        return bullet.rect.colliderect(enemy.rect)

    def handle_collisions(self, game):
        spaceship = game.spaceship
        spaceship_hit = False

        for enemy in game.enemy_handler.enemies[:]:
            if self.spaceship_enemy_collision(spaceship, enemy):
                if not spaceship.shield_active:
                    spaceship.is_alive = False
                    game.game_over = True 
                    break

        if spaceship_hit:
            spaceship.is_alive = False
            spaceship.reset_position()
            game.playing = False
            game.game_over_menu = GameOverMenu(game.score.value, game.score.max_score, game.score.enemies_eliminated)
            game.game_over = True 
        else:
            for bullet in spaceship.bullets[:]:
                for enemy in game.enemy_handler.enemies[:]:
                    if self.bullet_enemy_collision(bullet, enemy):
                        spaceship.bullets.remove(bullet)
                        game.enemy_handler.enemies.remove(enemy)
                        game.score.increase_score(15)
                        game.score.increase_enemies_eliminated()
                        game.score.update_max_score()
                        break

            for bullet in game.enemy_handler.bullets[:]:
                if self.bullet_enemy_collision(bullet, spaceship):
                    if not spaceship.shield_active:
                        spaceship.is_alive = False
                        game.game_over = True 
                        break
