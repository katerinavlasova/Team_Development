import random

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
##             Случайное число [0,1]
##    thirst - Жажда
##             Случайное число [0,1]
##    hunger - Голод
##             Случайное число [0,1]
##    social - Общение
##             Случайное число [0,1]


##  Методы класса:
##    dance - Танцевать
##    drink - Попить
##    eat   - Поесть
##    communicate - Общаться

gender_choise = ['m', 'f']
male_names = ['Dick']
female_names = ['Jessy']
game_lvl = 1

# Класс Person
class Person:
    
    print ("Я родился!")

    gender = random.choice(gender_choise)
    
    if gender == 'm':
        avatar = 'img/screen4/persons/boy/little.png'
        sprite = 'img/screen4/persons/boy/boy.png'
        name = random.choice(male_names)
    if gender == 'f':
        avatar = 'img/screen4/persons/girl/little.png'
        sprite = 'img/screen4/persons/girl/girl.png'
        name = random.choice(male_names)

    #needs
    dance  = random.random() / game_lvl
    thirst = random.random() / game_lvl
    hunger = random.random() / game_lvl
    social = random.random() / game_lvl        

    
    # создаем методы класса
    
    def dance(self):
        self.dance += 0.5 / game_lvl
        if self.dance > 1:
            self.dance = 1
        #show_dance(self.dance)
        
    def drink(self):
        self.thirst += 0.5 / game_lvl
        if self.thirst > 1:
            self.thirst = 1
        #show_thirst(self.thirst)
 
    def eat(self):
        self.hunger += 0.5 / game_lvl
        if self.hunger > 1:
            self.hunger = 1
        #show_hunger(self.hunger)

    def communicate(self):
        self.social += 0.5 / game_lvl
        if self.sotial > 1:
            self.sotial = 1
        #show_social(self.social)
