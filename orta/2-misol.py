# Hayvonot Classlari
# OTA_Class: Hayvon
# Xususiyatlar: turi, vazni
# Method: ovoz chiqarish (abstrakt)
# BOLA_Classlar: It, Mushuk
# It: ovoz sifatida "vov-vov"
# Mushuk: ovoz sifatida "miyov-miyov"
# Shart: Turli hayvonlarning ovoz chiqarishini model qiling.

class Hayvon:
    def __init__(self, type: str, weight: float)->None:
        self.__type = type
        self.__weight = weight

class It(Hayvon):
    def __init__(self, type, weight):
        super().__init__(type, weight)
        self.__ovoz = "Vov vov"
    def getter_ovoz(self):
        return self.__ovoz
class Mushuk(Hayvon):
    def __init__(self, type, weight):
        super().__init__(type, weight)
        self.__ovoz = "Miyav miyav"
    def getter_ovoz(self):
        return self.__ovoz
# Mushuk obyektini e`lon qilamiz
mushuk1 = Mushuk("Mushuk", 4)

# mushuk obyektini ovoz chiqarish methodiga murojaat qilamiz
print(mushuk1.getter_ovoz())

# It obyektini e`lon qilamiz
it1 = It("It", 20)

# It obyektini ovoz chiqarish methodiga murojaat qilamiz
print(it1.getter_ovoz())