import pygame
from Sofa_Class import *
from menu import *


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
        self.exit = ExitMenu(self)
        self.curr_menu = self.main_menu
        self.icon = pygame.image.load('img/screen4/persons/boy/little.png')
        pygame.display.set_icon(self.icon)

    def game_loop(self):
        while self.playing:
            self.check_events()
            if self.START_KEY:
                self.playing= False
            self.display = pygame.image.load('img/screen4/house/home_bg_1.png')
            resources = pygame.sprite.Group()
            divan = Sofa()
            resources.add(divan)
            #self.display.fill(self.BLACK)
            #self.draw_text('тут что-то будет....', 100, self.DISPLAY_W/2, self.DISPLAY_H/2)
            self.window.blit(self.display, (0,0))
            self.window.blit(divan.image, divan.rect)
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
