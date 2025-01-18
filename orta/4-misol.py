from pprint import pprint
# Kitobdo‘kon Classi
# Elementlar:
# Do‘kon nomi
# Joylashuvi
# Kitoblar ro‘yxati
# Xizmatlar
# Shart:
# Kitoblar ro‘yxatida ilmiy kitoblar bo‘lgan do‘konlar haqida ma'lumot chiqaring.

class Book_shop:
    Book_block = {}
    def __init__(self, name_shop: str, address: str)->None:
        self.name_shop = name_shop
        self.address = address
        self.__Books_list = []
    # dukonga kitob qo`shish uchun method
    def add_book(self, name: str, category: str, discription: str)->None:
        #Agar kiritgan ma`lumotlarimiz bo`sh bo`lmasa
        if name.strip() and category.strip() and discription.strip():
            self.Book_block = {
                'name': name,
                'category': category,
                'discription': discription
            }
            self.__Books_list.append(self.Book_block)
        else:
            print("Siz ma`lummot sifatida bo`sh nom kiritdingiz!")
    # Dukon kitoblarini chiqaruvchi method
    def get_books(self)-> list:
        # agar dukonda kitoblarimiz mavjud bo`lsa bizga ruyxatni qaytarsin
        if len(self.__Books_list) != 0:
            return self.__Books_list
        else:
            print("Dukonda birorta ham kitob yuq")
# dukonlarni saqlash uchun list yaratib olamiz
Shops_list = []


# Dukon bir nomli obyekt yatatamiz
dukon1 = Book_shop("Start_books", "samarqand city")
# bu dukonga bir nechta kitob qo`shamiz
dukon1.add_book("savdogarlar ustoz", "ilmiy", "maqsadi yuqlar maqsadi norlarga hizmat qiladi")
dukon1.add_book("Osmon ortida", "Janr", "Meni mendan emas, mazlumdan so`ra")
Shops_list.append(dukon1)


# Dukon2 nomli obyekt yatatamiz
dukon2 = Book_shop("Najot_books", "Kerpichka")
# bu dukonga bir nechta kitob qo`shamiz
dukon2.add_book("C tili", "ilmiy", "Algaritimlash asoslari mavjud")
dukon2.add_book("Bolaligim", "Janr", "Tog bag`ridagi hovlidagi yoshlar o`ylari")
Shops_list.append(dukon2)


# Dukon3 nomli obyekt yatatamiz
dukon3 = Book_shop("Afrosiyob", "Andalus street")
# bu dukonga bir nechta kitob qo`shamiz
dukon3.add_book("qorovulning kaliti", "detiktiv", ">>>>")
dukon3.add_book("Bola boshidan", "ibrat", ".......")
Shops_list.append(dukon3)

for dukon in Shops_list:    
    y = list(filter(lambda x: x['category'] == "ilmiy", dukon.get_books()))
    if len(y) != 0:
        print(dukon.name_shop)
    