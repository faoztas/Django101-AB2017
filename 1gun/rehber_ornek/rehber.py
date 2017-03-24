class Rehber:
    def __init__(self):
        self.kisiler = {}

    def ekle(self, kisi):
        self.kisiler[kisi.eposta] = kisi

    def epostaya_gore_ara(self, eposta):
        try:
            return self.kisiler[eposta]
        except KeyError:
            print ("bulunamadi")