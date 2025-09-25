from carres import Carre
from forme import Forme

class Long(Forme):

    num = 2

    def __init__(self,couleur):

       super().__init__(couleur, [  Carre(self,couleur, 460, 200),
                                    Carre(self,couleur, 500, 200),
                                    Carre(self,couleur, 540, 200),
                                    Carre(self,couleur, 580, 200)])
    
    def miseEnJeux(self):
        self.listeCarres[0].rect.x = 200
        self.listeCarres[0].rect.y = -40

        self.listeCarres[1].rect.x = 240
        self.listeCarres[1].rect.y = -40

        self.listeCarres[2].rect.x = 200
        self.listeCarres[2].rect.y = 0

        self.listeCarres[3].rect.x = 240
        self.listeCarres[3].rect.y = 0
