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
        self.running, self.playing = True, False  # цикл
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.DISPLAY_W, self.DISPLAY_H = 1280, 720  # разрешение экрана
        self.display = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H))
        self.window = pygame.display.set_mode(((self.DISPLAY_W, self.DISPLAY_H)))
        self.font_name = pygame.font.get_default_font()
        self.BLACK, self.WHITE = (255, 192, 200), (255, 255, 255)
        self.main_menu = MainMenu(self)
        self.levels = LevelsMenu(self)
        self.lvl_length = 60  # time, seconds
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
        resources = pygame.sprite.Group()
        divan = Sofa()
        dancefloor = Dancing()
        voda = Drinks()
        food = Food()
        resources.add(divan)
        resources.add(dancefloor)
        resources.add(voda)
        resources.add(food)
        moving = False
        moving_pers = False
        while self.playing:
            for event in pygame.event.get():
                if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                    print("мышь")
                    for pers in persons:
                        if pers.rect.collidepoint(event.pos):
                            print("НАЖАЛИ НА ЧЕЛА")
                            moving = True
                            moving_pers = pers  # заполмнили, какого персонажа двигаем
                            break
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        self.playing = False
                    if event.key == pygame.K_RETURN:
                        self.start = time.time()
                        self.pause()
                        self.end = time.time()
                        timer.time_beg += (self.end - self.start)
                if (moving == True):
                    mouse_position = pygame.mouse.get_pos()
                    moving_pers.set_coordinats(mouse_position[0], mouse_position[1])
                if (event.type == pygame.MOUSEBUTTONUP and event.button == 1):
                    moving = False

                    # персонаж не должен висеть в воздухе/быть за пределами экрана
                    if (moving_pers.rect.x < 95):
                        moving_pers.rect.x = 125
                    elif (moving_pers.rect.x > 1130):
                        moving_pers.rect.x = 1100
                    if (moving_pers.rect.y < 408 and moving_pers.rect.y > 150):
                        moving_pers.rect.y = 408
                    elif (moving_pers.rect.y > 408):
                        moving_pers.rect.y = 408
                    elif (moving_pers.rect.y < 150):
                        moving_pers.rect.y = 150

            self.check_events()
            self.display = pygame.image.load('img/screen4/house/home_bg_white_frame.png')
            # end of the game
            if timer.time_is_over(self):
                count_persons = len(persons)
                all_dance = 0
                all_thirst = 0
                all_hunger = 0
                all_social = 0
                for pers in persons:
                    all_social += pers.get_social()
                    all_dance  += pers.get_dance()
                    all_hunger += pers.get_hunger()
                    all_thirst += pers.get_thirst()
                result_needs = (all_hunger + all_dance + all_social + all_thirst) / (4*count_persons)
                print(result_needs)
                if result_needs > 50: # выигрыш
                    self.end_image = pygame.image.load('img/screen5/good/text.png')
                    self.gift_image = pygame.image.load('img/screen5/good/diamond.png')
                    self.gift_image = pygame.transform.scale(self.gift_image, (333, 222))
                else:
                    self.end_image = pygame.image.load('img/screen5/ugh/text.png')
                    self.gift_image = pygame.image.load('img/screen5/ugh/nothing.png')

                self.paused = True
                while self.paused:
                    self.rect1 = self.end_image.get_rect()
                    self.rect1.center = (640, 260)

                    self.rect2 = self.gift_image.get_rect()
                    self.rect2.center = (640, 480)

                    self.running, self.playing = False, False

                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            print("нажали на выход из окна завершения игры")
                            self.paused = False
                            self.curr_menu.run_display = True
                            g = Game()

                            while g.running:
                                g.curr_menu.display_menu()
                                g.game_loop()
                            break
                    self.check_events()

                    self.window.blit(self.end_image, self.rect1)
                    self.window.blit(self.gift_image, self.rect2)
                    pygame.display.update()

            self.window.blit(self.display, (0, 0))
            self.window.blit(divan.image, divan.rect)
            self.window.blit(voda.image, voda.rect)
            self.window.blit(dancefloor.image, dancefloor.rect)
            self.window.blit(food.image, food.rect)
            self.window.blit(timer.image, timer.rect)
            if (moving_pers):
                moving_pers.show_needs(self)

            for i in range(PERS_COUNT):
                self.window.blit(person_group[i].image, person_group[i].rect)
            # pygame.display.update() #обновляем дисплей

            hit_list = pygame.sprite.spritecollide(voda, persons, False)
            if (hit_list):
                for pers in hit_list:
                    voda.increase(pers)
            for pers in persons:
                if pers not in hit_list:
                    pers.dec_thirst()

            hit_list = pygame.sprite.spritecollide(divan, persons, False)
            if (hit_list):
                for pers in hit_list:
                    divan.increase(pers)
            for pers in persons:
                if pers not in hit_list:
                    pers.dec_social()

            hit_list = pygame.sprite.spritecollide(dancefloor, persons, False)
            if (hit_list):
                for pers in hit_list:
                    dancefloor.increase(pers)
            for pers in persons:
                if pers not in hit_list:
                    pers.dec_dance()

            hit_list = pygame.sprite.spritecollide(food, persons, False)
            if (hit_list):
                for pers in hit_list:
                    food.increase(pers)
            for pers in persons:
                if pers not in hit_list:
                    pers.dec_hunger()
            pygame.display.update()  # обновляем дисплей
            self.reset_keys()

    def pause(self):
        self.paused = True
        while self.paused:
            self.pause_image = pygame.image.load('img/screen6/text.png')
            self.rect = self.pause_image.get_rect()
            self.rect.center = (640, 360)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # конец игры
                    self.running, self.playing = False, False
                    self.curr_menu.run_display = False
                if event.type == pygame.KEYDOWN:
                    print("нажали на кпноку")
                    if event.key == pygame.K_RETURN:
                        print("валим с паузы")
                        self.paused = False
            self.check_events()
            self.window.blit(self.pause_image, self.rect)
            pygame.display.update()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # конец игры
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

    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)