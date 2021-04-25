from Person import *

INC_DRINKS = 20

class Drinks:
    inc = INC_DRINKS

    def increase(self, person):
        curr = person.get_thirst()
        person.set_thirst(self.inc + curr)
        return 0

if __name__ == "__main__":
    pers = Person()
    print(pers.get_thirst())
    voda = Drinks()
    print(voda.increase(pers))
    print(pers.get_thirst())
