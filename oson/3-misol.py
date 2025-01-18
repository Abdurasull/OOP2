from colorama import Fore, Style, Back
class Hayvon:
    def __init__(self, name: str, age: int)->None:
        self.name = name
        self.age = age
    def malumot(self)->str:
        return f"Hayvonning turi: {self.name}\nHayvonning yoshi: {self.age}"


class Yirqich(Hayvon):
    def __init__(self, type, age, hunting_style):
        super().__init__(type, age)
        self.hunting_style = hunting_style

    def hunting(self):
        print(f"{super().malumot()}\n{self.hunting_style} usuli bilan hujum qilyabdi\n" )

class Otxur(Hayvon):
    def __init__(self, type, age, food):
        super().__init__(type, age)
        self.food = food

    def eating(self):
        print(f"{super().malumot()}\n{self.food} yiyabdi" )

yirqich1 = Yirqich("Bo`ri", 4, "Kuzatib birdan tashlanadi")

Otxur1 = Otxur("Qo`y", 1, "arpa")

yirqich1.hunting()

Otxur1.eating()

