from Person import *

INC_SOCIAL = 20

class Sofa:
    inc = INC_SOCIAL

    def increase(self, person):
        curr = person.get_social()
        person.set_social(self.inc + curr)
        return 0


if __name__ == "__main__":
    pers = Person()
    print(pers.get_social())
    divan = Sofa()
    print(divan.increase(pers))
    print(pers.get_social())
