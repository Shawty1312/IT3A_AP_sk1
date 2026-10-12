import random

class Zvire:
    def __init__(self, jmeno:str, vek:int, misto:str = "bouda"): #self je pro jeden konkrétní objekt               #za = je misto ktery se pripise kdyz nenapiseme misto
        self.jmeno = jmeno
        self.vek = vek
        self.misto = misto 
        pass

    def zvuk(self):
        return "???"
    
    def predstav_se(self):
        return f"Jmenuji se {self.jmeno}, je mi {self.vek}"
    
    def kde_jsi(self):
        return f"Jsem v místě zvaném {self.misto}"
    
    def jdi_na(self, misto2:str = "zahrada"):
        self.misto = misto2    #zmeni misto na novy misto jde tam a pak tam i je
        return f"Jdu na {misto2}. {self.kde_jsi()}"
    
class Pes(Zvire):
    def __init__(self, jmeno, vek, plemeno, misto = "bouda"):
        super().__init__(jmeno, vek, misto)   #super odkazuje na tridu zvire (bere si metodu z rodice)
        self.plemeno=plemeno

    def zvuk(self):
        return "Haf, Haf!"
    
    def aport(self):
        return f"{self.jmeno} přinesla míček."
    
    def vycesat(self):
        if(random.randint(0,1)>0):
            return f"{self.jmeno} utekla před tvým kartáčem"
        else:
            return f"{self.jmeno} se nechala vyčesat"
        
    def predstav_se(self):
        return f"{super().predstav_se()} a jsem {self.plemeno}"      #super().predstav_se() vrátí nám to co je ve tride u zvirete
    
rita=Pes("Rita", 5, "Pitbull", "bouda")

print(rita.jmeno)
print(rita.plemeno)
print(rita.zvuk())
print(rita.predstav_se())    #má přístup ke zroji tridy nad nim
print(rita.aport())
print(rita.vycesat())
print(rita.kde_jsi())

print("-" *20)

class Kocka(Zvire):
    def __init__(self, jmeno, vek, barva, misto):
        super().__init__(jmeno, vek, misto)
        self.barva=barva
    
    def zvuk(self):
        return "Mňau Mňau"
    
    def utok(self):
        return f"Kočka {self.jmeno} tě naštvaně poškrábala"
        
    def pohlazeni(self):
        if(random.randint(0,1)>0):
            return self.utok
        else:
            return f"{self.jmeno} se nechala pohladit"
    
bella=Kocka("Bella", 3, "Černá", "Košík")

print(bella.jmeno)
print(bella.vek)
print(bella.barva)
print(bella.zvuk())
print(bella.utok())
print(bella.pohlazeni())
print(bella.jdi_na("parapet okna"))

print("-" *20)

class Papousek(Zvire):
    def __init__(self, jmeno, vek, barva_peri, misto = "klec"):
        super().__init__(jmeno, vek, misto)
        self.barva_peri=barva_peri

    def zvuk(self):
        return "Aeer Aeeer!"
    
    def opakuj(self, slovo:str):
        return f"{self.jmeno} opakuje: {slovo}! {slovo}!"
    
pepa=Papousek("Pepa", 1, "Červenozelený")

print(pepa.jmeno)
print(pepa.vek)
print(pepa.misto)
print(pepa.zvuk())
print(pepa.opakuj("Ahoj"))
    
print("-" *20)

class Had(Zvire):
    def __init__(self, jmeno, vek, delka_cm:int, jedovaty:bool, misto = "terárium"):
        super().__init__(jmeno, vek, misto)
        self.delka_cm=delka_cm
        self.jedovaty=jedovaty

    def zvuk(self):
        return "Sssssssss"
    
    def ustknuti(self):
        if self.jedovaty:
            return f"POZOR! {self.jmeno} tě uštknul a je jedovatý!"
        else:
            return f"{self.jmeno} tě kousnul, ale naštěstí není jedovatý!"
        
    def predstav_se(self):
        if self.jedovaty:
            typ = "jedovatý"
        else:
            typ= "škrtič"

        return f"Ssssss ... já jsem {self.jmeno}, měřím {self.delka_cm} a jsem {self.jedovaty}"
    
nagini=Had("Nagini", 2, 57, False)

print(nagini.zvuk())
print(nagini.ustknuti())
print(nagini.predstav_se())
    
print("-" *20)

zvire = Zvire("Luděk", 22)   #zvire bude obsahovat objekt s velkym Z a do zavorky vypiseme vse co je v zavorce v Zvire
print(zvire.jmeno)
print(zvire.vek)
print(zvire.zvuk())   # je to metoda takže přidáme ještě závorky za zvukem
print(zvire.predstav_se())
print(zvire.kde_jsi())
print(zvire.jdi_na("škola"))

print("-" *20)

zvire2 = Zvire("Lukáš", 17, "Louny")
print(zvire2.jmeno)
print(zvire2.vek)
print(zvire2.misto)
print(zvire2.zvuk())
print(zvire2.predstav_se())
print(zvire2.kde_jsi())
print(zvire2.jdi_na("oběd"))

print("-" *20)

ZOO = [rita, bella, pepa, nagini]

for obyvatel in ZOO:
    print(obyvatel.zvuk())
    print(obyvatel.predstav_se())  #polymorfismus 
    print("-" *20)