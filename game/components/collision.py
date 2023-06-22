
from game.utils.constants import BLACK

class CollisionHandler:

    def spaceship_enemy_collision(spaceship, enemy):
        return spaceship.rect.colliderect(enemy.rect)

    def spaceship_life_collision(spaceship, life):
        return spaceship.rect.colliderect(life.rect)

    def bullet_enemy_collision(bullet, spaceship):
        return bullet.rect.colliderect(spaceship.rect)

    def handle_collisions(self, game):
        spaceship = game.spaceship

        for enemy in game.enemy_handler.enemies[:]:
            if CollisionHandler.spaceship_enemy_collision(spaceship, enemy):
                if not spaceship.shield_active:
                    game.playing = False
                break

            for bullet in spaceship.bullets[:]:
                if CollisionHandler.bullet_enemy_collision(bullet, enemy):
                    spaceship.bullets.remove(bullet)
                    game.enemy_handler.enemies.remove(enemy)
                    game.score.increase_score(15)  # Aumentar la puntuación en 15 puntos por enemigo eliminado
                    break

        for bullet in game.enemy_handler.bullets[:]:
            if CollisionHandler.bullet_enemy_collision(bullet, spaceship):
                if not spaceship.shield_active:
                    game.playing = False
                break

        for life in game.power_handler.lifes[:]:
            if CollisionHandler.spaceship_life_collision(spaceship, life):
                if spaceship.life < 3:
                    spaceship.increment_life()
                    game.power_handler.lifes.remove(life)
                break
