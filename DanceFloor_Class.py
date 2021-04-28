import pygame
from Person import *

INC_LEISURE = 20

class Dancing(pygame.sprite.Sprite):
    inc = INC_LEISURE
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/screen4/places/leisure_refill.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (920, 487)
        self.image.set_colorkey((255, 255, 255))
    def increase(self, person):
        curr = person.get_dance()
        person.set_dance(self.inc + curr)
        return 0

if __name__ == "__main__":
    pers = Person()
    print(pers.get_dance())
    tysa = Dancing()
    print(tysa.increase(pers))
    print(pers.get_dance())
