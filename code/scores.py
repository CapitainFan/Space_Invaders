from pygame import font
from pygame.sprite import Group

from hp import Hp


class Scores:
    def __init__(self, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (255, 255, 255)
        self.bg_color = (0, 0, 0)
        self.font = font.SysFont(None, 36)
        self.image_score()
        self.image_best_score()
        self.image_hp()

    def image_score(self):
        self.score_img = self.font.render(str(self.stats.score),
                                          True, self.text_color,
                                          self.bg_color)
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.score_rect.right + 500
        self.score_rect.top = 20

    def image_best_score(self):
        self.best_score_img = self.font.render(str(self.stats.best_score),
                                               True, self.text_color,
                                               self.bg_color)
        self.best_score_rect = self.best_score_img.get_rect()
        self.best_score_rect.centerx += 300
        self.best_score_rect.top = 20

    def image_hp(self):
        self.hps = Group()
        for hp_number in range(self.stats.hp_left):
            hp = Hp(self.screen)
            hp.rect.x = 15 + hp_number * hp.rect.width
            hp.rect.y = 20
            self.hps.add(hp)

    def show(self):
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.best_score_img, self.best_score_rect)
        self.hps.draw(self.screen)
