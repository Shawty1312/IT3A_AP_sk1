class SitoveZarizeni:
    def __init__(self, nazev:str, ip_adresa:str, online:bool):
        self.nazev = nazev
        self.ip_adresa = ip_adresa
        self.online = online
        pass

    #def zmen_stav(self):
        #if self.online:


    def diagnostika(self):
        return f"Spouštím obecnou diagnostiku zařízení {self.nazev}."
    
