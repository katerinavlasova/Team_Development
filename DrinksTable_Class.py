import pygame
from Person import *

INC_DRINKS = inc_const

class Drinks(pygame.sprite.Sprite):
    inc = INC_DRINKS
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/screen4/places/drink_refill.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (260, 520)
        self.image.set_colorkey((255, 255, 255))
    def increase(self, person):
        curr = person.get_thirst()
        person.set_thirst(self.inc + curr)
        return 0

if __name__ == "__main__":
    pers = Person()
    print(pers.get_thirst())
    voda = Drinks()
    print(voda.increase(pers))
    print(pers.get_thirst())
