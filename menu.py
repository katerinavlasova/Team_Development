import pygame
import sys

class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = - 300

    def draw_cursor(self):
        self.game.draw_text('~', 150, self.cursor_rect.x - 50, self.cursor_rect.y)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()

class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start"
        self.startx, self.starty = self.mid_w, self.mid_h -200
        self.levelsx, self.levelsy = self.mid_w, self.mid_h
        self.exitx, self.exity = self.mid_w, self.mid_h + 200
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

    def display_menu(self):
        self.run_display = True
        #pygame.mixer.music.load('music/wet-fingers-turn-me-on.mp3')
        #pygame.mixer.music.set_volume(0.4)  # 1=100%
        #pygame.mixer.music.play(-1)
        while self.run_display:
            self.game.check_events()
            self.check_input()

            self.game.display = pygame.image.load('img/screen1/backgroung_screen1_1.jpg')

            self.game.draw_text("Start Game", 80, self.startx+50, self.starty)
            self.button_play = pygame.image.load('img/screen1/button_play.png')
            self.button_play = pygame.transform.scale(self.button_play, (100, 100))
            self.b1 = self.button_play.get_rect(
                bottomright=(450, 210))
            self.game.display.blit(self.button_play, self.b1)

            self.game.draw_text("Levels", 80, self.levelsx+20, self.levelsy)
            self.button_levels = pygame.image.load('img/screen1/button_setting.png')
            self.button_levels = pygame.transform.scale(self.button_levels, (140, 140))
            self.b2 = self.button_levels.get_rect(
                bottomright=(520, 420))
            self.game.display.blit(self.button_levels, self.b2)

            self.game.draw_text("Exit", 80, self.exitx+20, self.exity)
            self.button_exit = pygame.image.load('img/screen1/button_exit.png')
            self.button_exit = pygame.transform.scale(self.button_exit, (100, 100))
            self.b2 = self.button_exit.get_rect(
                bottomright=(560, 600))
            self.game.display.blit(self.button_exit, self.b2)

            self.draw_cursor()
            self.blit_screen()


    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.levelsx + self.offset, self.levelsy)
                self.state = 'Levels'
            elif self.state == 'Levels':
                self.cursor_rect.midtop = (self.exitx + self.offset, self.exity)
                self.state = 'Exit'
            elif self.state == 'Exit':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
        elif self.game.UP_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.exitx + self.offset, self.exity)
                self.state = 'Exit'
            elif self.state == 'Levels':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
            elif self.state == 'Exit':
                self.cursor_rect.midtop = (self.levelsx + self.offset, self.levelsy)
                self.state = 'Levels'

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Start':
                self.game.playing = True
            elif self.state == 'Levels':
                self.game.curr_menu = self.game.levels
            elif self.state == 'Exit':
                self.game.curr_menu = self.game.exit
            self.run_display = False

class LevelsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Level1'
        self.lev1x, self.lev1y = self.mid_w, self.mid_h + 20
        self.lev2x, self.lev2y = self.mid_w, self.mid_h + 40
        self.cursor_rect.midtop = (self.lev1x + self.offset+200, self.lev1y-35)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display = pygame.image.load('img/screen1/backgroung_screen1_3.jpg')
            self.game.draw_text('Levels', 80, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 120)
            self.game.draw_text("Level1", 60, self.lev1x, self.lev1y - 20)
            self.game.draw_text("Level2", 60, self.lev2x, self.lev2y + 80)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == 'Level1':
                self.state = 'Level2'
                self.cursor_rect.midtop = (self.lev2x + self.offset+200, self.lev2y+70)
            elif self.state == 'Level2':
                self.state = 'Level1'
                self.cursor_rect.midtop = (self.lev1x + self.offset+200, self.lev1y-35)
        elif self.game.START_KEY:
            pass


class ExitMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        pygame.quit()
        sys.exit()
