import pygame
import random

dec_const = 0.03
inc_const = 0.15

##  Атрибуты класса:
##    gender - Пол.
##             Cимвол 'm' или 'f'
##    avatar - Маленькая авочка, будет светиться при выборе персонажа.
##             Путь до изображения. Строка
##    sprite - Перс во весь рост, будет на игровом поле.
##             Путь до изображения. Строка
##    name -   Имя. Строка
##
##    dance  - Танцы
##             Случайное число [0,100]
##    thirst - Жажда
##             Случайное число [0,100]
##    hunger - Голод
##             Случайное число [0,100]
##    social - Общение
##             Случайное число [0,100]

##  Методы класса:
## dec_* - уменьшение уровня потребности (в течение времени)
## set_* - установка уровня потребности из внешних классов (мест пополнения)
## get_* - передача значения

gender_choise = ['m', 'f']
y_coord_choise = [500, 245]
male_names = ['Dick']
female_names = ['Jessy']
game_lvl = 1

# Класс Person
class Person(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        gender = random.choice(gender_choise)
    
        if gender == 'm':
            self.avatar = pygame.image.load('img/screen4/persons/boy/little.png').convert_alpha()
            self.image = pygame.image.load('img/screen4/persons/boy/boy.png').convert_alpha()
            self.name = random.choice(male_names)
        if gender == 'f':
            self.avatar = pygame.image.load('img/screen4/persons/girl/little.png').convert_alpha()
            self.image = pygame.image.load('img/screen4/persons/girl/girl.png').convert_alpha()
            self.name = random.choice(female_names)

        #needs
        self.dance  = random.randint(0,100) // game_lvl
        self.thirst = random.randint(0,100) // game_lvl
        self.hunger = random.randint(0,100) // game_lvl
        self.social = random.randint(0,100) // game_lvl 

        self.rect = self.image.get_rect()
        y_coord = random.choice(y_coord_choise)
        x_coord = random.uniform(250, 920)
        self.rect.center = (x_coord, y_coord)
        self.image.set_colorkey((255, 255, 255))
    #print ("Я родился!")       

        
    # создаем методы класса
    
    def dec_dance(self):
        self.dance -= dec_const
        if self.dance > 100:
            self.dance = 100
        elif self.dance < 0:
            self.dance = 0
        #show_dance(self.dance)
        
    def dec_thirst(self):
        self.thirst -= dec_const
        if self.thirst > 100:
            self.thirst = 100
        elif self.thirst < 0:
            self.thirst = 0
        #show_thirst(self.thirst)
 
    def dec_hunger(self):
        self.hunger -= dec_const
        if self.hunger > 100:
            self.hunger = 100
        elif self.hunger < 0:
            self.hunger = 0
        #show_hunger(self.hunger)

    def dec_social(self):
        self.social -= dec_const
        if self.social > 100:
            self.social = 100
        elif self.social < 0:
            self.social = 0        
        #show_social(self.social)

    def set_dance(self, val):
        if (val > 100):
            self.dance = 100
        elif (val < 0):
            self.dance = 0
        else:
            self.dance = val

    def set_thirst(self, val):
        if (val > 100):
            self.thirst = 100
        elif (val < 0):
            self.thirst = 0
        else:
            self.thirst = val

    def set_hunger(self, val):
        if (val > 100):
            self.hunger = 100
        elif (val < 0):
            self.hunger = 0
        else:
            self.hunger = val

    def set_social(self, val):
        if (val > 100):
            self.social = 100
        elif (val < 0):
            self.social = 0
        else:
            self.social = val

    def get_dance(self):
        return(self.dance)

    def get_thirst(self):
        return(self.thirst)

    def get_hunger(self):
        return(self.hunger)

    def get_social(self):
        return(self.social)
    def set_coordinats(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def show_needs(self, screen):
        a = self.thirst
        b = self.dance
        c = self.hunger
        d = self.social

        a_x, a_y = 282, 651
        b_x, b_y = 282, 687
        c_x, c_y = 752, 651
        d_x, d_y = 752, 687

        a_coord = (a_x, a_y)
        b_coord = (b_x, b_y)
        c_coord = (c_x, c_y)
        d_coord = (d_x, d_y)

        a_font_x = a_x + int(a / 100 * 373)
        b_font_x = b_x + int(b / 100 * 373)
        c_font_x = c_x + int(c / 100 * 373)
        d_font_x = d_x + int(d / 100 * 373)

        a_font_coord = (a_font_x, a_y)
        b_font_coord = (b_font_x, b_y)
        c_font_coord = (c_font_x, c_y)
        d_font_coord = (d_font_x, d_y)

        frame_coord = (0, 644)

        line_img = pygame.image.load('img/screen4/bg/line.png').convert_alpha()
        font_img = pygame.image.load('img/screen4/bg/font.png').convert_alpha()
        frame_img = pygame.image.load('img/screen4/bg/frame.png').convert_alpha()
        ffont_img = pygame.image.load('img/screen4/bg/frame_font.png').convert_alpha()

                
        screen.window.blit(ffont_img, frame_coord)       
        screen.window.blit(line_img, a_coord)
        screen.window.blit(font_img, a_font_coord)
        screen.window.blit(line_img, b_coord)
        screen.window.blit(font_img, b_font_coord)
        screen.window.blit(line_img, c_coord)
        screen.window.blit(font_img, c_font_coord)
        screen.window.blit(line_img, d_coord)
        screen.window.blit(font_img, d_font_coord)
        screen.window.blit(frame_img, frame_coord)
        screen.window.blit(self.avatar, (144, 656))
