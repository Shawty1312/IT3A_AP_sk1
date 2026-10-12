import random


class Vozidlo:
    def __init__(self, znacka:str, rok_vyroby:int, stav_nadrze:int = "100"):
        self.znacka = znacka
        self.rok_vyroby = rok_vyroby
        self.stav_nadrze = stav_nadrze
        pass

    def zvuk_motoru(self):
        return "???"
    
    def info(self):
        return f"Vozidlo {self.znacka}, rok výroby {self.rok_vyroby}."
    
    def startuj(self):
        if(random.randint(0,1)>0):
            return f"Auto je nastartováno, {self.zvuk_motoru()}."
        else:
            return f"Došel benzín."
        
vozidlo = Vozidlo("Volkswagen", 2002)
print(vozidlo.znacka)
print(vozidlo.rok_vyroby)
print(vozidlo.stav_nadrze)
print(vozidlo.zvuk_motoru())
print(vozidlo.info())
print(vozidlo.startuj())
# ----------------------------------------------------------------------------------------------------------#

class Auto(Vozidlo):
    def ___init__(self, znacka, rok_vyroby, stav_nadrze, typ_prevodovky:str):
        super().__init__(znacka, rok_vyroby, stav_nadrze)
        self.typ_prevodovky = typ_prevodovky

    def zvuk_motoru(self):
        return "Vrum vrum!"

    def zatrub(self):
        return "Tůtůůt"
    
    def info(self):
        return f"Auto {self.znacka}, rok výroby {self.rok_vyroby}."
    
auto = Auto("BMW", 1997, 62)         #nejde dodat převodovka
print(auto.znacka)
print(auto.rok_vyroby)
print(auto.stav_nadrze)
print(auto.zvuk_motoru())
print(auto.zatrub())
print(auto.info())
# ---------------------------------------------------------------------------------------------------------#

class Moped(Vozidlo):
    def ___init__(self, znacka, rok_vyroby, stav_nadrze, ma_slapadla:bool):
        super().__init__(znacka, rok_vyroby, stav_nadrze)
        self.ma_slapadla = ma_slapadla

    def zvuk_motoru(self):
        return "Trrrrr!"
    
    def slapej(self):                                 #nejde
        if self.ma_slapadla:
            typ = "šlapu"
        else:
            typ = "nešlapu"

        return f"Zrovna na mopedu {self.ma_slapadla}."
    
    def info(self):
        return f"Moped {self.znacka}, rok výroby {self.rok_vyroby}."
    
moped = Moped("Pioneer", 1865, 23)       #nejde dát šlapání
print(moped.znacka)
print(moped.rok_vyroby)
print(moped.stav_nadrze)
print(moped.zvuk_motoru())
print(moped.info)

Garaz = [auto, moped]

for parkovani in Garaz:
    print(parkovani.info())
    print(parkovani.startuj())