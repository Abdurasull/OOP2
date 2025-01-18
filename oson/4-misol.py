class Avto:
    def __init__(self, nomi: str, marka: str, narx: float):
        self.__nomi = nomi
        self.__marka = marka
        self.__narx = narx
    def setter_name(self, nome)->None:
        self.__nomi = nome 
    def setter_mark(self, marka)->None:
        self.__marka = marka
    def setter_price(self, price)->None:
        self.__narx = price
    def getter(self):
        if not self.__nomi.strip() and self.__marka.strip:
            return f"Mashina markasi: {self.__marka}\nMashina nomi: {self.__nomi}\nMashina narxi: {self.__narx}$\n"
        else:
            return "Ma`lumotlar bo`sh kiritilgan"
# ma`lumotlar bo`sh kiritilganda hato ishlashini tikshirish uchun
mashina1 = Avto("nexia 3", "  ", 10000)
print(mashina1.getter())

# endi setter orqali ma`lumotlarni o`zgartirib chiqarib ko`ramiz
mashina1.setter_name("Cobalt")
mashina1.setter_mark("Chevrolet")
mashina1.setter_price(10000)

# ma`lumotni chiqarib ko`ramiz
print(mashina1.getter())