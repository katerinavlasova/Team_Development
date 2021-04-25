import pygame
import time


class Timer(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/screen4/places/communion_refill.png').convert_alpha()
        self.rect = (91, 8)
        self.image.set_colorkey((255, 255, 255))
        self.time_beg = time.time()
    def time_is_over(self, game):
        self.time_del = int(time.time() - self.time_beg)
        if self.time_del > game.lvl_length:
            return True
        else:
            self.img_name = 'img/screen4/timer/' + str(game.lvl_length - self.time_del) + '.png'
            #print(self.img_name)
            self.image = pygame.image.load(self.img_name)
            return False
