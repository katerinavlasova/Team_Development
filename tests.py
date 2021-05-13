#!/usr/bin/python3.7.10
import unittest
from Person import *
from Sofa_Class import *
from FoodTable_Class import *
from DrinksTable_Class import *
from DanceFloor_Class import *

class PersonTests(unittest.TestCase):
    pygame.init()
    screen = pygame.display.set_mode((100,100))
    pers = Person()
    def test_set_dance_normal(self):
        self.pers.set_dance(50)
        self.assertEqual(self.pers.dance, 50)
    def test_set_dance_less(self):
        self.pers.set_dance(-50)
        self.assertEqual(self.pers.dance, 0)
    def test_set_dance_more(self):
        self.pers.set_dance(150)
        self.assertEqual(self.pers.dance, 100)

    def test_set_thirst(self):
        self.pers.set_thirst(50)
        self.assertEqual(self.pers.thirst, 50)
    def test_set_thirst_less(self):
        self.pers.set_thirst(-50)
        self.assertEqual(self.pers.thirst, 0)
    def test_set_thirst_more(self):
        self.pers.set_thirst(150)
        self.assertEqual(self.pers.thirst, 100)

    def test_set_hunger(self):
        self.pers.set_hunger(50)
        self.assertEqual(self.pers.hunger, 50)
    def test_set_hunger_less(self):
        self.pers.set_hunger(-50)
        self.assertEqual(self.pers.hunger, 0)
    def test_set_hunger_more(self):
        self.pers.set_hunger(150)
        self.assertEqual(self.pers.hunger, 100)

    def test_set_social(self):
        self.pers.set_social(50)
        self.assertEqual(self.pers.social, 50)
    def test_set_social_less(self):
        self.pers.set_social(-50)
        self.assertEqual(self.pers.social, 0)
    def test_set_social_more(self):
        self.pers.set_social(150)
        self.assertEqual(self.pers.social, 100)

    def test_get_dance(self):
        self.pers.dance = 50
        self.assertEqual(self.pers.get_dance(), 50)
    def test_get_thirst(self):
        self.pers.thirst = 50
        self.assertEqual(self.pers.get_thirst(), 50)
    def test_get_hunger(self):
        self.pers.hunger = 50
        self.assertEqual(self.pers.get_hunger(), 50)
    def test_get_social(self):
        self.pers.social = 50
        self.assertEqual(self.pers.get_social(), 50)

    def test_dec_dance(self):
        curr = self.pers.dance
        self.pers.dec_dance()
        self.assertEqual(self.pers.dance, curr - dec_const)
    def test_dec_hunger(self):
        curr = self.pers.hunger
        self.pers.dec_hunger()
        self.assertEqual(self.pers.hunger, curr - dec_const)
    def test_dec_thirst(self):
        curr = self.pers.thirst
        self.pers.dec_thirst()
        self.assertEqual(self.pers.thirst, curr - dec_const)
    def test_dec_social(self):
        curr = self.pers.social
        self.pers.dec_social()
        self.assertEqual(self.pers.social, curr - dec_const)

    def test_dec_dance_less(self):
        self.pers.dance = 0
        self.pers.dec_dance()
        self.assertEqual(self.pers.dance, 0)
    def test_dec_hunger_less(self):
        self.pers.hunger = 0
        self.pers.dec_hunger()
        self.assertEqual(self.pers.hunger, 0)
    def test_dec_thirst_less(self):
        self.pers.thirst = 0
        self.pers.dec_thirst()
        self.assertEqual(self.pers.thirst, 0)
    def test_dec_social(self):
        self.pers.social = 0
        self.pers.dec_social()
        self.assertEqual(self.pers.social, 0)

    def test_set_coor_x(self):
        self.pers.set_coordinats(100, 100)
        self.assertEqual(self.pers.rect.x, 100)
    def test_set_coor_y(self):
        self.pers.set_coordinats(100, 100)
        self.assertEqual(self.pers.rect.y, 100)

class Sofa_Class_Tests(unittest.TestCase):
    pygame.init()
    screen = pygame.display.set_mode((100,100))
    sofa = Sofa()
    pers = Person()

    def test_increase(self):
        curr = self.pers.social
        self.sofa.increase(self.pers)
        self.assertEqual(self.pers.social, curr + INC_SOCIAL)

class Food_Table_Class_Tests(unittest.TestCase):
    pygame.init()
    screen = pygame.display.set_mode((100,100))
    foodtable = Food()
    pers = Person()

    def test_increase(self):
        curr = self.pers.hunger
        self.foodtable.increase(self.pers)
        self.assertEqual(self.pers.hunger, curr + INC_SOCIAL)

class Drinks_Table_Class_Tests(unittest.TestCase):
    pygame.init()
    screen = pygame.display.set_mode((100,100))
    drinkstable = Drinks()
    pers = Person()

    def test_increase(self):
        curr = self.pers.thirst
        self.drinkstable.increase(self.pers)
        self.assertEqual(self.pers.thirst, curr + INC_SOCIAL)

class Dance_Floor_Class_Tests(unittest.TestCase):
    pygame.init()
    screen = pygame.display.set_mode((100,100))
    dancefloor = Dancing()
    pers = Person()

    def test_increase(self):
        curr = self.pers.dance
        self.dancefloor.increase(self.pers)
        self.assertEqual(self.pers.dance, curr + INC_SOCIAL)

if __name__ == "__main__":
    unittest.main()
