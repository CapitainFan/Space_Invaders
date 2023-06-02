import pygame

import controls

from pygame.sprite import Group

from scores import Scores
from gun import Gun
from stats import Stats


def run():
    pygame.init()
    pygame.display.set_caption('Space Invaders')
    screen = pygame.display.set_mode((650, 660))
    back_ground_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    aliens = Group()
    controls.create_enemies(screen, aliens)
    stats = Stats()
    score = Scores(screen, stats)

    while True:
        controls.events(screen, gun, bullets)
        if stats.run_game:
            gun.update_gun()
            controls.update(back_ground_color, screen, stats,
                            score, gun, aliens, bullets)
            controls.update_bullets(screen, stats, score, bullets, aliens)
            controls.update_aliens(stats, screen, score, gun, aliens, bullets)


run()
