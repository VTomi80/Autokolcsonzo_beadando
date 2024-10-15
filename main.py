from Autok import Auto
from Autok import szemelyauto, teherauto
from Berles import Berles
from Berlo import Berlo
from Kolcsonzo import Kolcsonzo
from datetime import date


def adatfeltoltes():

    kolcsonzo = Kolcsonzo("VargaRent")

    auto1 = szemelyauto("Trabant 601", "ABC-123", 20000, 4, "Benzin")
    auto2 = szemelyauto("Lada 2107", "BBC-007", 30000, 5, "Benzin")
    auto3 = szemelyauto("Skoda 105", "CIA-001", 25000, 5, "Benzin")
    auto4 = teherauto("Kamaz", "BBW-113", 50000, 6000, True)

    berlo1 = Berlo("AB123456", "Pista Bacsi", "B", "0670123456")
    berlo2 = Berlo("AB654321", "Joska Bacsi", "C", "0670654321")

    kolcsonzo.uj_berlo(berlo1)
    kolcsonzo.uj_berlo(berlo2)

    kolcsonzo.uj_auto(auto1)
    kolcsonzo.uj_auto(auto2)
    kolcsonzo.uj_auto(auto3)
    kolcsonzo.uj_auto(auto4)

    kolcsonzo.auto_berles("ABC-123", "AB123456", "2024-11-01", 3)
    kolcsonzo.auto_berles("BBC-007", "AB654321", "2024-10-15", 5)
    kolcsonzo.auto_berles("BBW-113", "AB654321", "2024-10-15", 2)

    return kolcsonzo


def interface(kolcsonzo):
    while True:
        print("\nAutókölcsönző menü:")
        print("1. Autó bérlése")
        print("2. Bérlés lemondása")
        print("3. Bérlések listázása")
        print("4. Kilépés")

        val = input("Válasszon a fenti menüből (1-4): ")

        if val == "1":
            rendszam = input("Adja meg az autó rendszámát: ")
            azonosito = input("Adja meg a jogosítványa számát: ")
            kezdet = input("Adja meg a bérlés dátumát (ÉÉÉÉ-HH-NN): ")
            napok = int(input("Adja meg a bérlés napjainak számát: "))
            kolcsonzo.auto_berles(rendszam, azonosito, kezdet, napok)

        elif val == "2":
            rendszam = input("Adja meg a lemondani kívánt autó rendszámát: ")
            datum = input(
                "Adja meg a lemondani kívánt bérlés kezdetének dátumát (YYYY-MM-DD): ")
            kolcsonzo.lemondas(rendszam, date(
                int(datum[0: 4]), int(datum[5: 7]), int(datum[8:])))

        elif val == "3":
            kolcsonzo.lista()

        elif val == "4":
            break

        else:
            print("Érvénytelen válasz.")


kolcsonzo = adatfeltoltes()
interface(kolcsonzo)
