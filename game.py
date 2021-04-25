import pygame
from Sofa_Class import *
from DanceFloor_Class import *
from DrinksTable_Class import *
from FoodTable_Class import *
from Person import *
from menu import *
from Timer_Class import *

PERS_COUNT = 3

class Game():
    def __init__(self):
        pygame.mixer.pre_init(44100, -16, 2)
        pygame.init()
        self.running, self.playing = True, False # цикл
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.DISPLAY_W, self.DISPLAY_H = 1280, 720 #разрешение экрана
        self.display = pygame.Surface((self.DISPLAY_W,self.DISPLAY_H))
        self.window = pygame.display.set_mode(((self.DISPLAY_W,self.DISPLAY_H)))
        self.font_name = pygame.font.get_default_font()
        self.BLACK, self.WHITE = (255, 192, 200), (255, 255, 255)
        self.main_menu = MainMenu(self)
        self.levels = LevelsMenu(self)
        self.lvl_length = 60 # time, seconds
        self.exit = ExitMenu(self)
        self.curr_menu = self.main_menu
        self.icon = pygame.image.load('img/screen4/persons/boy/little.png')
        pygame.display.set_icon(self.icon)

    def game_loop(self):
        timer = Timer()
        game_params = pygame.sprite.Group()
        game_params.add(timer)
        person_group = [0] * PERS_COUNT
        persons = pygame.sprite.Group()
        for i in range(PERS_COUNT):
            person_group[i] = Person()
            persons.add(person_group[i])
        while self.playing:
            self.check_events()
            if self.START_KEY:
                self.playing= False
            self.display = pygame.image.load('img/screen4/house/home_bg_white_frame.png')
            #timer            
            if timer.time_is_over(self):
                break
            resources = pygame.sprite.Group()
            divan = Sofa()
            dancefloor = Dancing()
            voda = Drinks()
            food = Food()
            
            resources.add(divan)
            resources.add(dancefloor)
            resources.add(voda)
            resources.add(food)
            
            self.window.blit(self.display, (0,0))
            self.window.blit(divan.image, divan.rect)
            self.window.blit(voda.image, voda.rect)
            self.window.blit(dancefloor.image, dancefloor.rect)
            self.window.blit(food.image, food.rect)
            self.window.blit(timer.image, timer.rect)
            for i in range(PERS_COUNT):
                self.window.blit(person_group[i].image, person_group[i].rect)
            pygame.display.update() #обновляем дисплей
            self.reset_keys()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #конец игры
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True

    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def draw_text(self, text, size, x, y ):
        font = pygame.font.Font(self.font_name,size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface,text_rect)
