from datetime import datetime
from Autok import Auto
from Berles import Berles
from Berlo import Berlo

class Kolcsonzo:
    def __init__(self, nev):
        self.nev = nev
        self.autok =  []
        self.berlesek = []
        self.berlok = []

    def uj_auto(self, auto:Auto):
        self.autok.append(auto)

    def uj_berlo(self, berlo:Berlo):
        self.berlok.append(berlo)

    def auto_berles(self, rendszam, berlo_id, kezdet, napok):
        for auto in self.autok:
            if auto.rendszam == rendszam and auto.elerheto:
                try:
                    datetime.strptime(kezdet, '%Y-%m-%d')
                except ValueError:
                    print("Helytelen dátumformátum. A szükséges formátum: YYYY-MM-DD")
                    return None

                # Keresd meg a bérlőt az ID alapján
                berlo = next((b for b in self.berlok if b.id == berlo_id), None)  # Frissítés itt
                if not berlo:
                    print("Nincs ilyen bérlő.")
                    return None

                uj_berles = Berles(auto, berlo, kezdet, napok)  # Itt auto és berlo kell, hogy objektumok legyen
                self.berlesek.append(uj_berles)
                print(f"Bérlés regisztrálva!")
                return uj_berles
        print("Az autó nem elérhető!")

    def lemondas(self, rendszam):
        for berles in self.berlesek:
            if berles.auto.rendszam == rendszam:
                berles.lemond()
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






