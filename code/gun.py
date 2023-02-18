import pygame
from pygame.sprite import Sprite


class Gun(Sprite):
    def __init__(self, screen):
        super(Gun, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('code/images/starship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False
        self.mleft = False

    def draw_gun(self):
        self.screen.blit(self.image, self.rect)

    def update_gun(self):
        if self.mright and self.rect.right < self.screen_rect.right:
            self.center += 1.25

        if self.mleft and self.rect.left > self.screen_rect.left:
            self.center -= 1.25

        self.rect.centerx = self.center

    def create_gun(self):
        self.center = self.screen_rect.centerx
