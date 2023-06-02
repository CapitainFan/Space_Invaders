import pygame
import sys
import time

from bullet import Bullet
from alien import Alien


def events(screen, gun, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                gun.mright = True
            elif event.key == pygame.K_LEFT:
                gun.mleft = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                gun.mright = False
            if event.key == pygame.K_LEFT:
                gun.mleft = False


def create_enemies(screen, aliens):
    alien = Alien(screen)
    alien_width = alien.rect.width
    alien_number_x = int((650 - 2 * alien_width) / alien_width)
    alien_hight = alien.rect.height
    alien_number_y = int((650 - 100 - 2 * alien_hight) / alien_hight)

    for row_number in range(alien_number_y-3):
        for alien_number in range(alien_number_x):
            alien = Alien(screen)
            alien.x = alien_width + alien_width * alien_number
            alien.y = alien_hight + alien_hight * row_number
            alien.rect.x = alien.x
            alien.rect.y = alien.rect.height + alien.rect.height * row_number
            aliens.add(alien)


def gun_kill(stats, screen, score, gun, aliens, bullets):
    if stats.hp_left > 1:
        stats.hp_left -= 1
        score.image_hp()
        aliens.empty()
        bullets.empty()
        create_enemies(screen, aliens)
        gun.create_gun()
        time.sleep(1)
    else:
        stats.run_game = False
        sys.exit()


def update(back_ground_color, screen, stats, score, gun, aliens, bullets):
    screen.fill(back_ground_color)
    score.show()

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    gun.draw_gun()
    aliens.draw(screen)
    pygame.display.flip()


def update_aliens(stats, screen, score, gun, aliens, bullets):
    aliens.update()

    if pygame.sprite.spritecollideany(gun, aliens):
        gun_kill(stats, screen, score, gun, aliens, bullets)

    aliens_check(stats, screen, score, gun, aliens, bullets)


def update_bullets(screen, stats, score, bullets, aliens):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if collisions:
        for aliens in collisions.values():
            stats.score += 10 * len(aliens)
        score.image_score()
        best_score_check(stats, score)
        score.image_hp()

    if len(aliens) == 0:
        bullets.empty()
        create_enemies(screen, aliens)


def aliens_check(stats, screen, score, gun, aliens, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            gun_kill(stats, screen, score, gun, aliens, bullets)
            break


def best_score_check(stats, score):
    if stats.score > stats.best_score:
        stats.best_score = stats.score
        score.image_best_score()
        with open('code/best_score.txt', 'w') as file:
            file.write(str(stats.best_score))
