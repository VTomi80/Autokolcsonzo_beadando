class Auto:
    def __init__(self, tipus, rendszam, dij):
        self.tipus = tipus
        self.rendszam = rendszam
        self.dij = dij
        self.elerheto = True #default érték, az autó létrehozásakor elérhető

class szemelyauto(Auto):
    def __init__(self, tipus, rendszam, dij, utas_szam, uzemanyag):
        super().__init__(tipus, rendszam, dij) #Az Auto absztrakt osztály, a saját attribútumokat itt adjuk a személyautó osztályhoz
        self.utas_szam = utas_szam
        self.uzemanyag = uzemanyag

def __str__(self):
    return f"Típus: {self.tipus}, Rendszám: {self.rendszam}, Dij: {self.dij}, Utasok száma: {self.utas_szam}, Üzemanyag: {self.uzemanyag}"

class teherauto(Auto):
    def __init__(self, tipus, rendszam, dij, teherbiras, billent:bool = False):
        super().__init__(tipus, rendszam, dij) #Az Auto absztrakt osztály, a saját attribútumokat itt adjuk a teherautó osztályhoz
        self.teherbiras = teherbiras
        self.billent = billent

    def __str__(self):
        return f"Típus: {self.tipus}, Rendszám: {self.rendszam}, Dij: {self.dij}, Teherbírás: {self.teherbiras}, Billent: {self.billent}"

