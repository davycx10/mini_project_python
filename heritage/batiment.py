class Batiment:
    
    def __init__(self, étage, adresse, noms):
        self.étage = étage
        self.adresse = adresse
        self.noms = noms       
    def get_étage(self):
        return self.étage
    
    def get_adresse(self):
        return self.adresse
    
    def get_noms(self):
        return self.noms
    

class Immeuble(Batiment):
    
    def __init__(self, étage, adresse, noms, balcons):
        super().__init__(étage, adresse, noms)
        
        self.balcons = balcons
        
    def get_balcons(self):
        return self.balcons 
    
    
class Supermarket(Batiment):
    
    def __init__(self, étage, adresse, noms, rayons, réserve):
        super().__init__(étage, adresse, noms) 
        self.rayons = rayons
        self.réserve = réserve
        
    def get_rayons(self):
        return self.rayons
    
    def get_réserve(self):
        return self.réserve
    
class Bank(Batiment):
    
    def __init__(self, étage, adresse, noms, coffre):
        super().__init__(étage, adresse, noms)    
        self.coffre = coffre
        
    def get_coffre(self):
        return self.coffre   