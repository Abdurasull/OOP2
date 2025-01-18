# SoftwareEngineer Klassini Yaratish
# 1. SoftwareEngineer nomli klassni yarating. U quyidagi atributlarga ega bo‘lsin:
# Surname (Familiyasi): Xodimning familiyasi.
# Position (Lavozimi): Xodimning lavozimi (Junior, Middle, Senior).
# Salary (Oyligi): Xodimning asosiy oyligi.

# 2. SoftwareEngineer Klassini Yaratish
# SoftwareEngineer nomli klassni yarating, u SoftwareEngineer klassidan voris bo‘lsin. Qo‘shimcha atributlar:
# Bonus (Ustama haqi): Oylikka qo‘shiladigan ustama.
# Department (Bo‘lim): Xodim qaysi bo‘limda ishlaydi (1-bo‘lim, 2-bo‘lim, yoki 3-bo‘lim).

# 3. Masala Sharti
# SoftwareEngineer klassidan 5 ta obyekt yarating va har birining quyidagi ma’lumotlarini foydalanuvchi kiritishi kerak:
# Familiyasi, lavozimi, asosiy oyligi, ustama haqi, va bo‘limi.
# Har bir bo‘lim uchun umumiy to‘langan maoshni hisoblang. Bu quyidagicha bo‘ladi:
# Umumiy maosh = asosiy oylik + ustama haqi.


class Developer:
    def __init__(self, Surname: str, Position: str, salary: float):
        self.Surname = Surname
        self.position = Position
        self.salary = salary

class SoftwareEngineer(Developer):
    def __init__(self, Surname, Position, salary, bonus, department):
        super().__init__(Surname, Position, salary)
        self.bonus = bonus
        self.department = department
    # Umumiy oylikni chiqaruvchi function
    def all_salary(self)->float:
        return self.salary + self.bonus
    
# hamma obyektlarni bitta listga olish uchun list yaratib olamiz
Software_engineer_list = []
Software_engineer_list.append(SoftwareEngineer("Abdurasul", "Junior", 500, 100, "3-bo`lim"))
Software_engineer_list.append(SoftwareEngineer("Nozim", "Meddle", 1000, 200, "1-bo`lim"))
Software_engineer_list.append(SoftwareEngineer("Asror", "Junior", 400, 70, "3-bo`lim")) 
Software_engineer_list.append(SoftwareEngineer("Eldor", "Junior", 300, 50, "3-bo`lim"))
Software_engineer_list.append(SoftwareEngineer("Abdulaziz", "Junior", 300, 50, "2-bo`lim"))

# Natijada har bir bo‘lim uchun jami maosh summasini chiqaring.
for i in range(3):
    list1 = list(filter(lambda x: x.department == f"{i+1}-bo`lim", Software_engineer_list))
    print(f"{i+1}-Bulim: {sum(list(map(lambda x: x.all_salary(), list1)))}")