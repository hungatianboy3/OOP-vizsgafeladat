from classes.Auto import *
class Szemelyauto(Auto):
    tipus = "Személyautó"
    def __init__(self, rendszam, berleti_dij):
        self.rendszam = rendszam
        self.berleti_dij = berleti_dij
        self.berlesek = []
    
 