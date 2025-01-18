# Book nomli class yarating.
# Unda quyidagi property (xususiyatlar) bo‘lsin:
# Name: Kitob nomi
# Page_count: Kitobning sahifalar soni
# Price: Kitobning narxi
# Ushbu classdan 5 ta obyekt yarating.
# Har bir obyekt uchun foydalanuvchi nom, sahifalar soni va narxni kiritishi kerak.
# Quyidagi amallarni bajaradigan methodlar yozing:
# Sahifa sonini oshirish: Har bir kitobning sahifa sonini 10 taga oshiradigan method yozing.
# Narxni kamaytirish: Agar sahifa soni 100 dan ko‘p bo‘lsa (oshirilganidan keyin), ushbu kitobning narxini 2 baravar kamaytiradigan method yozing.
# Natijada barcha obyektlarning yangi ma’lumotlarini ekranga chiqaring.
class Book:
    def __init__(self, name: str, Page_count: int, Price: int )->None:
        self.name = name
        self.Page_count = Page_count
        self.Price = Price

    def add_pages(self):
        self.Page_count += 10

    def narx_kamaytir(self, kamayish_miqdor):
        if  kamayish_miqdor >= self.Price:
            print("Bunchalik kamaytira olmaysiz, iltimos kichikroq narxga kamaytirib ko`ring")
        else:
            if self.Page_count > 100:
                if kamayish_miqdor * 2 < self.Price:
                    self.Price -= kamayish_miqdor * 2
                else:
                    self.Price -= kamayish_miqdor
# kitob1 nomli obyekt yaratamiz
kitob1 = Book("Savdogarlar ustozi", 250, 150000)

# bu obyekni sahifalar sonini oshiramiz
kitob1.add_pages()

# Bu kitobni narxini kamaytiramiz
kitob1.narx_kamaytir(10000)

# obyektimizni yangi holatini ifodalaymiz
print(f"Kitoni nomi: {kitob1.name}\nKitobni sahifalar soni: {kitob1.Page_count}\nKitobni narxi: {kitob1.Price}")
