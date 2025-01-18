# Taksi Classi
# Elementlar:
# Public: Haydovchi ismi, Mashina nomi
# Private: Narx, Yo‘nalish, Bo‘sh joylar soni
# Shartlar:
# Getter yordamida narxni oling.
# Setter yordamida bo‘sh joylarni yangilang (agar 0 dan kam bo‘lsa, xato xabar chiqaring).
# Haydovchi va mashina nomini bevosita oling va o‘zgartiring.

class Taxi:
    def __init__(self, name_driver: str, name_car: str, price: int , yunalish: str, place_count: int ):
        self.name_driver = name_driver
        self.name_car = name_car
        self.__price = price
        self.__yunalish = yunalish
        self.__place_count = place_count
    # Narxni olamiz
    def getter_price(self):
        return self.__price
    # Bo`sh joylarni yangilaymiz
    def setter_place(self, place_count):
        if place_count < 0:
            print("Bo`sh joy 0 dan kichik bo`lmasligi kk")
        else:
            self.__place_count = place_count
    # bo`sh joylarni chiqarish uchun
    def get_place(self):
        return self.__place_count

# taxi nomli obyekt yaratamiz
taxi = Taxi("Asror", "Avtobus", 2000, "Kaftarxona", 10)

# setter yordamida bo`sh joylarni yangilaymiz(mumkin bo`lmagan hjolatni ham kiritish bilan)
taxi.setter_place(-2)
# endi esa mumkin bo`lgan holat bilan
taxi.setter_place(7)

# haydovchini o`zgartiramiz va natijani ekranga chiqaramiz
taxi.name_driver = "Abdulaziz"

print(f"Haydovchi: {taxi.name_driver}\nmashina: {taxi.name_car}\nbo`sh joylar: {taxi.get_place()}\n")