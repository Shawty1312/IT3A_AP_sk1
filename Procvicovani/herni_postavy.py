import random

class Postava:
    def __init__(self, jmeno:str, zdravi:int):
        self.jmeno = jmeno
        self.zdravi = zdravi
        pass

    def predstav_se(self):
        return f"Jmenuji se {self.jmeno}, {self.zdravi}."
    
    def utok(self):
        return f"0"
    
postava = Postava("?", 3)
print(postava.utok())
    
class Rytir(Postava):
    def __init__(self, jmeno, zdravi, brneni:int):
        super().__init__(jmeno, zdravi)
        self.brneni = brneni

    def utok(self):
        if(random.randint(10,20)>10<20):
            return f"Seknutí mečem."
        else:
            return f"Minul."
        
rytir = Rytir("Rytíř", 3, 1)
print(rytir.jmeno)
print(rytir.zdravi)
print(rytir.predstav_se())
print(rytir.utok())

print("-"*20)

class Mag(Postava):
    def __init__(self, jmeno, zdravi, mana:int):
        super().__init__(jmeno, zdravi)
        self.mana = mana

    def utok(self):
        return super().utok()
    
    