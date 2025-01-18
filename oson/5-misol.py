class Transport:
    def __init__(self, name: str) -> None:
        self.name = name

    def drive_avtobus(self):
        print("Avtobus harakatlandi\n")

    def drive_Poyizd(self):
        print("Poyizd harakatlandi\n")

class Avtobuz(Transport):
    def __init__(self, name):
        super().__init__(name)

class Poyizd(Transport):
    def __init__(self, name):
        super().__init__(name)


poyizd = Poyizd("Afrosiyob")
poyizd.drive_Poyizd()

avtobuz = Avtobuz("UzAvto")
avtobuz.drive_avtobus()