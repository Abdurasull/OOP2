# Mashina Classi
# Elementlar:
# Public: Model, Rangi
# Private: Tezlik, Narx, Yoqilg‘i turi
# Shartlar:
# Getter orqali tezlikni ko‘rsating.
# Yoqilg‘i turini setter orqali o‘zgartiring.
# Model va rangni bevosita oling va o‘zgartiring.

class Mashina:
    def __init__(self, Modil: str, color: str, tizlik: int, price: float, yoqilgi_turi: str):
        self.Model = Modil
        self.color = color
        self.__tizlik = tizlik
        self.__price = price
        self.__Yoqilgi = yoqilgi_turi
    # getter_tizlik orqli tezlikni chiqaramiz
    def getter_tizlik(self):
        print(f"{self.Model} tizligi: {self.__tizlik}km/soat\n")
    # setter_yoqilgi orqali yoqilgini o`zgartiramiz`
    def setter_yoqilgi(self, yoqilgi):
        self.__Yoqilgi = yoqilgi

# mashina obyektini yaratib ko`ramiz
mashina = Mashina("Avtobus", "Oq", 80, 2000, "dezil")

# mashinani tezligini chiqaramiz
mashina.getter_tizlik()

# mashinani rangi vamodilini o`zgartiramiz va ekranga chop etamiz
mashina.color = "Qora"
mashina.Model = "K5"

mashina.getter_tizlik()