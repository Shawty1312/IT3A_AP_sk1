class Robot:
    def __init__(self, oznaceni:str, baterie:int, ukol:str = "opravit součástky"):
        self.oznaceni = oznaceni
        self.baterie = baterie
        self.ukol = ukol
        pass

    def zvuk(self):
        return "???"
    
    def diagnostika(self, baterie2:int = 74):
        return f"Mé označení je {self.oznaceni}, můj stav baterie je {baterie2}."
    
    def aktualni_ukol(self):
        return f"Můj aktuální úkol je {self.ukol}."
    
    def zadej_ukol(self, ukol2:str = "umýt nádobí"):
        self.ukol = ukol2
        return f"Můj nový ůkol je {ukol2}. {self.aktualni_ukol()}"

robot = Robot ("RBT-17", 87)
print(robot.zvuk())
print(robot.baterie)
print(robot.diagnostika())
print(robot.aktualni_ukol())
print(robot.zadej_ukol())