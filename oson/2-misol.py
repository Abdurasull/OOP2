from colorama import Fore, Style, Back
from datetime import datetime

class Phon_number:
    def __init__(self):
        self.__phon_nubers = []

    def add_number(self, name: str, number: str)->None:
        # agar kiritilgan ma`lumotlar bo`sh bo`lmasa bazaga qo`shsiz
        if name.strip() and number.strip():
            self.__phon_nubers.append({
                'name': name,
                'number': number
            })
            hozzirgi_vaqt = datetime.now()
            result_time = hozzirgi_vaqt.strftime("%Y-%m-%d  %H:%M:%S")
            with open("2-misol.txt", "a") as file:
                file.write(f"ruyxatga olingan vaqti: {result_time}\nIsmi: {name}\nPhon number: {number}\n\n")
        else:
            print(f"{Fore.RED}Siz ma`lumot sifatida bo`sh qiymat yubormoqchi bo`ldingiz{Fore.RESET}\n")

    def get_numbers(self)->list:
        if len(self.__phon_nubers) == 0:
            print(f"{Fore.RED}Hali birorta ham Ma`lumot kiritilmagan{Fore.RESET}\n\n")
        else:
            return self.__phon_nubers


kontakt1 = Phon_number()
kontakt1.add_number("Abdurasul", "+998 33 9969631")
kontakt1.add_number("Asror", "+998 77 0456903")
kontakt1.add_number("Mexriddin", "+998 66 776688")
kontakt1.add_number("   ", "+998 95 6667788")

result = kontakt1.get_numbers()
if result:
    for number in result:
        print(f"Ismi: {number['name']}\nTelefoni: {number['number']}\n\n")