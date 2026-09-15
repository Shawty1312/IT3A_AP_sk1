class Hrdina:
    def __init__(self, jmeno:str, lvl:int, lokace:str = "obloha"):
        self.jmeno = jmeno
        self.lvl = lvl
        self.lokace = lokace
        pass

    def pokrik(self):
        return "???"
    
    def predstav_se(self):
        return f"Jmenuji se {self.jmeno}."
    
    def kde_jsi(self):
        return f"Jsem v místě zvaném {self.lokace}."
    
    def presun_se(self, lokace2:str = "město"):
        self.lokace = lokace2
        return f"Přesouvám se na místo zvané {lokace2}. {self.kde_jsi()}"
    
hrdina = Hrdina ("Spiderman", 5)
print(hrdina.jmeno)
print(hrdina.lvl)
print(hrdina.lokace)
print(hrdina.pokrik())
print(hrdina.predstav_se())
print(hrdina.kde_jsi())
print(hrdina.presun_se())