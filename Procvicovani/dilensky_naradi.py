class Naradi:
    def  __init__(self, znacka:str, model:str):
        self.znacka = znacka
        self.model = model
        pass

    def identifikace(self):
        return f"{self.znacka}, {self.model}"
    
    def pracuj(self):
        return f"Právě pracuju."
    
naradi = Naradi("Parkside","2026")
print(naradi.identifikace())
print(naradi.pracuj())