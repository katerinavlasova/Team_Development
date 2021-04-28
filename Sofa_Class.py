import pygame
from Person import *

INC_SOCIAL = 20

class Sofa(pygame.sprite.Sprite):
    inc = INC_SOCIAL
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/screen4/places/communion_refill.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (537, 520)
        self.image.set_colorkey((255, 255, 255))
    def increase(self, person):
        curr = person.get_social()
        person.set_social(self.inc + curr)
        return 0


if __name__ == "__main__":
    pers = Person()
    print(pers.get_social())
    divan = Sofa()
    print(divan.increase(pers))
    print(pers.get_social())
