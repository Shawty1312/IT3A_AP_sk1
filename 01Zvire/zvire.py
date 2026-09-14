class Zvire:
    def __init__(self, jmeno:str, vek:int, misto:str = "bouda"): #self je pro jeden konkrétní objekt               #za = je misto ktery se pripise kdyz nenapiseme misto
        self.jmeno = jmeno
        self.vek = vek
        self.misto = misto 
        pass

zvire = Zvire("Luděk", 22)   #zvire nude obsahovat objekt s velkym Z a do zavorky vypiseme vse co je v zavorce v Zvire
print(zvire.jmeno)
print(zvire.vek)