import pygame


class Alien(pygame.sprite.Sprite):
    def __init__(self, screen) -> None:
        super(Alien, self).__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load('code/images/alien.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        # self.mr = True
        # self.ml = False
        # self.mdown = False
        self.is_update = 0

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.is_update > 700:
            self.y += 30
            self.rect.y = self.y
            self.is_update = 0
        else:
            self.is_update += 1

    # def update_02(self):
    #     if self.x+50 >= self.screen_rect.right:
    #         self.ml = True
    #         self.mr = False
    #     elif self.x <= self.screen_rect.left:
    #         self.mr = True
    #         self.ml = False

    #     if self.mr:
    #         self.x += 0.5
    #     if self.ml:
    #         self.x -= 0.5

    #     self.rect.x = self.x

    # def update_03(self):
    #     if self.mdown:
    #         self.y += 50
    #         if self.x <= self.screen_rect.left:
    #             self.mr = True
    #             self.mdown = False
    #         else:
    #             self.ml = True
    #             self.mdown = False

    #     elif self.ml:
    #         self.x -= 0.5
    #         if self.x <= self.screen_rect.left:
    #             self.mdown = True
    #             self.ml = False

    #     elif self.mr:
    #         self.x += 0.5
    #         if self.x+50 >= self.screen_rect.right:
    #             self.mdown = True
    #             self.mr = False

    #     self.rect.x = self.x
    #     self.rect.y = self.y
