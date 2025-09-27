from .carres import Carre
from .forme import Forme

class Long(Forme):

    num = 2

    def __init__(self, couleur, orientation):

       super().__init__(couleur, orientation, [  
                                    Carre(couleur, 460, 200),
                                    Carre(couleur, 500, 200),
                                    Carre(couleur, 540, 200),
                                    Carre(couleur, 580, 200)]
                        )
    
    def miseEnJeux(self):
        self.listeCarres[0].rect.x = 160
        self.listeCarres[0].rect.y = 0

        self.listeCarres[1].rect.x = 200
        self.listeCarres[1].rect.y = 0

        self.listeCarres[2].rect.x = 240
        self.listeCarres[2].rect.y = 0

        self.listeCarres[3].rect.x = 280
        self.listeCarres[3].rect.y = 0

        super().miseEnJeux()
