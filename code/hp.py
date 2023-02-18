import pygame
from pygame.sprite import Sprite


class Hp(Sprite):
    def __init__(self, screen):
        super(Hp, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('code/images/hp.png')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
