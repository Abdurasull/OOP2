# O‘quv Markazi Classlari
# OTA_Class: O‘quvMarkazi
# Method: dars o‘tkazish (abstrakt)
# BOLA_Classlar: ITMarkazi, TilMarkazi
# ITMarkazi: dasturlash darslari o‘tkazadi
# TilMarkazi: xorijiy til darslari o‘tkazadi
# Shart: Har bir markazda turli xil darslar o‘tkaziladi.

class Oquv_markaz:
    def dars_methodi(self, usuli: str)-> str:
        return f"{usuli} darslari o`tgaziladi\n"
    
class ITmarkazi(Oquv_markaz):
    __markaz_nomi = "Dasturlash"
    def dars_methodi(self):
        return super().dars_methodi(self.__markaz_nomi)

class Tilmarkazi(Oquv_markaz):
    __markaz_nomi = "Xorijiy til"
    def dars_methodi(self):
        return super().dars_methodi(self.__markaz_nomi)

# IT obyektini e`lon qilib olamiz
IT = ITmarkazi()
# IT obyektini dars_methodi ga murojat qilamiz
print(IT.dars_methodi())

# Til obyektini e`lon qilib olamiz
Til = Tilmarkazi()
# Til obyektini dars_methodi ga murojat qilamiz
print(Til.dars_methodi())
