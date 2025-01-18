from datetime import datetime

# 1 -  masala
# Avtomobil Classi:
# Public: Model, Rang
# Private: Narx, Marka, Ishlab chiqarilgan yil
# Shartlar: 
# Getter bilan narx va ishlab chiqarilgan yilni ko‘rsating.
# Setter yordamida narxni yangilang (agar yangi narx manfiy bo‘lsa, xato xabar chiqaring).

class Avtomabil:
    def __init__(self, Modil: str, color: str, price: int, marka: str, year: int):
        self.Modil = Modil
        self.color = color
        self.__price = price
        self.__marka = marka
        self.__year = year

    def getter(self)->str:
        with open("1-misol.txt", "a") as file:
            hozirgi_vaqt = datetime.now()
            result_time = hozirgi_vaqt.strftime("%Y-%m-%d  %H:%M:%S")
            file.write(f"Faylga joylangan sana: {result_time}\nNarxi: {self.__price}$, Ishlab chiqarilgan: {self.__year}\n\n")
        return f"Narxi: {self.__price}$, Ishlab chiqarilgan: {self.__year}\n\n"

    def setter(self, price: int)->None:
        if price > 0:
            self.__price = price
        else:
            print("Siz mashina narxini manfiy son qila olmaysiz\n\n")

# Avto1 nomli obyekt yaratildi
avto1 = Avtomabil("cherlolit", "oq", 10000, "Cobolt", 2018)

# natijani ekranga chiqaramiz
print(avto1.getter())

# setter methodi yordamida avto1 ni narxini o`zgartiramiz
avto1.setter(12)
# natijani ekranga chiqaramiz
print(avto1.getter())


