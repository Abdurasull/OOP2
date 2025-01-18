# Laptop Class:
# Laptop classini yarating, atributlari:
# brand,
# price,
# battery_life (batareya vaqti, soatlarda).
# Quyidagi metodlarni yozing:
# apply_discount(percent) — narxini percent ga pasaytirsin.
# Agar batareya vaqti 5 soatdan kam bo‘lsa, narxini 10% pasaytiruvchi metod qo‘shing.

class Laptop:
    def __init__(self, brand: str, price: float, battery_life: float)->None:
        self.__brand = brand
        self.__price = price
        self.__battery_life = battery_life
    # narni percent qiymatga kamaytirish
    def apple_discount(self, percent)->None:
        if self.__price > percent:
            self.__price -= percent
        else:
            print("Siz aytgan summaga kamaytirsak telefonni tikinga va olganingiz uchun sizga qo`shimcha pul berishga ham turi keladi\n")
    # agar batariya quvvati 5 soatdan kam bo`lsa narxni yana 10 foizga tushurib beradi
    def impact_price(self):
        if self.__battery_life < 5:
            self.__price -= self.__price * 0.1
    # barcha ma`lumotlarni qaytarish uchun function
    def getter(self)->str:
        return f"Komputer: {self.__brand}\nNarxi: {self.__price}$\nQuvvati: {self.__battery_life}soat\n"


# Laptop nomli obyekt yaratamiz
laptop = Laptop("HUAWEI", 800, 4)

# NARXINI 100$ ga tushuramiz
laptop.apple_discount(100)

# natijani ko`rishimiz mumkin
print(laptop.getter())

# agar quvvati 5 soatdan kam bo`lsa narxiga ta`sirini ko`rish
laptop.impact_price()

# natijani ko`rishimiz mumkin
print(laptop.getter())
