from carres import Carre
from forme import Forme

class Cube(FOrme):

    num = 1

    def __init__(self,game,couleur):

        super().__init__(couleur, [ Carre(self,couleur, 500, 180),
                                    Carre(self,couleur, 540, 180),
                                    Carre(self,couleur, 500, 220),
                                    Carre(self,couleur, 540, 220)])
    
    def miseEnJeux(self):
        self.listeCarres[0].rect.x = 200
        self.listeCarres[0].rect.y = -40

        self.listeCarres[1].rect.x = 240
        self.listeCarres[1].rect.y = -40

        self.listeCarres[2].rect.x = 200
        self.listeCarres[2].rect.y = 0

        self.listeCarres[3].rect.x = 240
        self.listeCarres[3].rect.y = 0
