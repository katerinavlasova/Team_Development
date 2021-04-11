from Person import *

INC_FOOD = 20

class Food:
    inc = INC_FOOD

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

