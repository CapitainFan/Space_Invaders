import pygame


class Alien(pygame.sprite.Sprite):
    def __init__(self, screen) -> None:
        super(Alien, self).__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load('code/images/alien_1.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.mr = True
        self.ml = False

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.y += 0.09
        self.rect.y = self.y

    def update_x(self):
        if self.x+50 >= self.screen_rect.right:
            self.ml = True
            self.mr = False
        elif self.x <= self.screen_rect.left:
            self.mr = True
            self.ml = False

        if self.mr:
            self.x += 0.9
        if self.ml:
            self.x -= 0.9

        self.rect.x = self.x
