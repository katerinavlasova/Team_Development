from Person import *

INC_LEISURE = 20

class Dancing:
    inc = INC_LEISURE

    def increase(self, person):
        curr = person.get_dance()
        person.set_dance(self.inc + curr)
        return 0

if __name__ == "__main__":
    pers = Person()
    print(pers.get_dance())
    tysa = Dancing()
    print(tysa.increase(pers))
    print(pers.get_dance())
