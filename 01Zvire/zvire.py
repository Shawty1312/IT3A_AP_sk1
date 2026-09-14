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

zvire = Zvire("Luděk", 22)   #zvire bude obsahovat objekt s velkym Z a do zavorky vypiseme vse co je v zavorce v Zvire
print(zvire.jmeno)
print(zvire.vek)
print(zvire.zvuk())   # je to metoda takže přidáme ještě závorky za zvukem
print(zvire.predstav_se())
print(zvire.kde_jsi())
print(zvire.jdi_na("škola"))

zvire2 = Zvire("Lukáš", 17, "Louny")
print(zvire2.jmeno)
print(zvire2.vek)
print(zvire2.misto)
print(zvire2.zvuk())
print(zvire2.predstav_se())
print(zvire2.kde_jsi())
print(zvire2.jdi_na("oběd"))