from datetime import datetime
from Autok import Auto
from Berles import Berles
from Berlo import Berlo
from datetime import timedelta


class Kolcsonzo:
    def __init__(self, nev):
        self.nev = nev
        self.autok = []
        self.berlesek = []
        self.berlok = []

    def uj_auto(self, auto: Auto):
        self.autok.append(auto)

    def uj_berlo(self, berlo: Berlo):
        self.berlok.append(berlo)

    def auto_berles(self, rendszam, berlo_id, kezdet, napok):
        try:
            kezdet_datum = datetime.strptime(kezdet, '%Y-%m-%d').date()
        except ValueError:
            print("Helytelen dátumformátum. A szükséges formátum: YYYY-MM-DD")
            return None

        auto = next((a for a in self.autok if a.rendszam == rendszam), None)
        if not auto:
            print("Az autó nem található!")
            return None

        for berles in self.berlesek:
            berles_kezdet = datetime.strptime(berles.kezdet, '%Y-%m-%d').date()
            berles_vege = berles_kezdet + timedelta(days=berles.napok)
            if berles.auto.rendszam == rendszam and not (kezdet_datum > berles_vege or kezdet_datum + timedelta(days=napok) < berles_kezdet):
                print("Az autó a megadott időszakban már foglalt!")
                return None

        berlo = next((b for b in self.berlok if b.id == berlo_id), None)
        if not berlo:
            print("Nincs ilyen bérlő.")
            return None

        uj_berles = Berles(auto, berlo, kezdet, napok)
        self.berlesek.append(uj_berles)
        auto.elerheto = False
        print("Bérlés regisztrálva!")
        return uj_berles

    def lemondas(self, rendszam, datum):
        for berles in self.berlesek:
            if berles.auto.rendszam == rendszam and str(datum) == str(berles.kezdet):
                self.berlesek.remove(berles)
                print(f"{rendszam} Bérlése törölve.")
                return

        print(f"A {rendszam} rendszámú autó nincs kibérelve.")

    def lista(self):
        if self.berlesek:
            for berles in self.berlesek:
                print(berles)
        else:
            print("Jelenleg nincsenek folyamatban bérlések.")
