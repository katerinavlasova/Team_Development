import pygame
from Person import *

INC_FOOD = inc_const

class Food(pygame.sprite.Sprite):
    inc = INC_FOOD
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/screen4/places/food_refill.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (530, 285)
        self.image.set_colorkey((255, 255, 255))
    def increase(self, person):
        curr = person.get_hunger()
        person.set_hunger(self.inc + curr)
        return 0

if __name__ == "__main__":
    pers = Person()
    print(pers.get_hunger())
    eda = Food()
    print(eda.increase(pers))
    print(pers.get_hunger())

