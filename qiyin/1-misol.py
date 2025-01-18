#  Robot Classi
# Elementlar:
# Public: Model raqami, Ishlovchi hududi
# Private: Zaryad darajasi, Maksimal ish vaqti, Status (Ishlayapti / Kutmoqda)
# Shartlar:
# Getter orqali zaryad darajasini ko‘rsating, lekin agar daraja 20% dan past bo‘lsa, "Zaryadlash kerak" xabari chiqsin.
# Maksimal ish vaqtini setter orqali yangilang, lekin bu 12 soatdan oshmasligi kerak.
# Statusni faqat getter orqali ko‘ring, "Kutmoqda" bo‘lsa, zaryadni avtomatik 100% ga o‘rnatish amalga oshsin.

class Robot:
    def __init__(self, Modil_raqami: str, work_region: str, Step_zaryad: int,max_work_time: int, status: str):
        self.Model_raqam  = Modil_raqami
        self.work_region = work_region
        self.__Step_zaryad = Step_zaryad
        self.__max_work_time = max_work_time
        self.__status = status
    def getter_zaryad(self):
        if self.__Step_zaryad < 20:
            print("Zaryadlash kerak\n")
        else:
            print(f"zaryad miqdori: {self.__Step_zaryad}%")
    def setter(self, work_time):
        if work_time <= 12 and work_time > 0:
            self.__max_work_time = work_time
        else:
            print("Ish vaqtini noto`g`ri kiritdingiz\n")
    def getter_status(self):
        print(self.__status)
        if self.__status == 'kutmoqda':
            self.__Step_zaryad = 100

roobit = Robot("N_1", 'samarqand shaxar', 19, 7,  "kutmoqda")

roobit.getter_zaryad()