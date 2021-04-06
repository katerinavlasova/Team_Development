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
    
    #print ("Я родился!")

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
    dance  = random.randint(0,100) // game_lvl
    thirst = random.randint(0,100) // game_lvl
    hunger = random.randint(0,100) // game_lvl
    social = random.randint(0,100) // game_lvl        

        
    # создаем методы класса
    
    def dance(self):
        self.dance += 50 // game_lvl
        if self.dance > 100:
            self.dance = 100
        #show_dance(self.dance)
        
    def drink(self):
        self.thirst += 50 // game_lvl
        if self.thirst > 100:
            self.thirst = 100
        #show_thirst(self.thirst)
 
    def eat(self):
        self.hunger += 50 // game_lvl
        if self.hunger > 100:
            self.hunger = 100
        #show_hunger(self.hunger)

    def communicate(self):
        self.social += 50 // game_lvl
        if self.sotial > 100:
            self.sotial = 100
        #show_social(self.social)

    def set_dance(self, val):
        self.dance = val

    def set_thirst(self, val):
        self.thirst = val

    def set_hunger(self, val):
        self.hunger = val

    def set_social(self, val):
        self.social = val

    def get_dance(self):
        return(self.dance)

    def get_thirst(self):
        return(self.thirst)

    def get_hunger(self):
        return(self.hunger)

    def get_social(self):
        return(self.social)
