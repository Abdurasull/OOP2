# Xodim ma’lumotlari" klassini yaratish
# Shart: Xodim nomli klass yarating. Bu klassda xodimning ism-familiyasi, yoshi, va lavozimi haqida ma’lumot saqlansin.
# Qoidalangan: Ma’lumotlarni o‘zgartirish uchun maxsus metodlar (getter va setter) yozing. Lavozimni o‘zgartirganda, yangi lavozim bo‘sh emasligini tekshiring.


class Xodim:
    def __init__(self, firstname, lastname, lavozim) -> None:
        self.__firstname = firstname #private ko`rinishda saqlndi ya`ni togridan tog`ri o`zgartirib bo`lmaydi
        self.__lastname = lastname
        self.__lavozim = lavozim
    #name ni chaqirish uchun 
    def getter_name(self):
        return self.__firstname
    #lastname ni chaqirish uchun
    def getter_lastname(self):
        return self.__lastname
    #lavozim ni chaqirish uchun
    def getter_lavozim(self):
        return self.__lavozim
    
    # Ma`lumotlarni o`zgartirish uchun
    def setter(self, firstname: str, lastname: str, lavozim: str) -> None:
        if firstname.strip() and lastname.strip() and lavozim.strip():
            self.__firstname = firstname
            self.__lastname = lastname
            self.__lavozim = lavozim
        else:
            print("O`zgartirmoqchi bo`lgan ma`lunotlaringiz ichida bo`sh ma`lumot bor")

xodim = Xodim("Abdurasul", "Salimov", "Raxbar")
print(f"Hodim ismi: {xodim.getter_name()}\nHodim familiyasi: {xodim.getter_lastname()}\nHodim lavozimi: {xodim.getter_lavozim()}\n\n")


print("O`zgartirildi")
xodim.setter("Abbos", "axrorov", "Operator")

print(f"Hodim ismi: {xodim.getter_name()}\nHodim familiyasi: {xodim.getter_lastname()}\nHodim lavozimi: {xodim.getter_lavozim()}\n\n")