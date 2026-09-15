class Motorka:
    def __init__(self, znacka:str, kategorie:str, stav_nadrze:int, stav_stojanku:str):
        self.znacka = znacka
        self.kategorie = kategorie
        self.stav_nadrze = stav_nadrze
        self.stav_stojanku = stav_stojanku
        pass

    def zatoc_plyn(self):
        return "VRRUM"
    
    def zmen_stojanek(self, stojanek2:str = "nahore"):
        self.stav_stojanku = stojanek2
        return f"Stojánek se dal {stojanek2}. {self.stav_stojanku()}"
   
            
motorka = Motorka ("Kawasaki", "silniční", 12, "dole")
print(motorka.zatoc_plyn())
print(motorka.znacka)
print(motorka.kategorie)
print(motorka.stav_stojanku)
print(motorka.zmen_stojanek())