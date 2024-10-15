from Autok import Auto
from Berlo import Berlo
from datetime import date


class Berles:
    def __init__(self, auto: Auto, berlo: Berlo, kezdet, napok: int):
        self.auto = auto
        self.berlo = berlo
        self.kezdet = kezdet
        self.napok = napok
        self.ar = auto.dij * napok
        self.vege = date(int(kezdet[0: 4]), int(kezdet[5: 7]), int(kezdet[8:]) + napok)

    def __str__(self):
        return f"Bérlő {self.berlo.nev}, Rendszám: {self.auto.rendszam}, Bérlés kezdete: {self.kezdet}, Bérlés vége: {self.vege}, Bérlés időtartama: {self.napok} nap"
