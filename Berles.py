from Autok import Auto
from Berlo import Berlo

class Berles:
    def __init__(self, auto:Auto, berlo:Berlo, kezdet, napok:int):
        self.auto = auto
        self.berlo = berlo
        self.kezdet = kezdet
        self.napok = napok
        self.ar = auto.dij * napok
        self.auto.elerheto = False

    def __str__(self):
        return f"Bérlő {self.berlo.nev}, Rendszám: {self.auto.rendszam}, Bérlés kezdete: {self.kezdet}, Bérlés időtartama: {self.napok} nap"

    def lemond(self):
        self.auto.elerheto = True




