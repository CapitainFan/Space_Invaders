import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, gun):
        super(Bullet, self).__init__()
        self.screen = screen
        self.gun = gun
        self.rect = pygame.Rect(0, 0, 1, 10)
        self.color_2 = (235, 57, 26)
        self.color = (166, 230, 29)
        self.speed = 10
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def update(self):
        self.y -= self.speed
        self.rect.y = self.y
