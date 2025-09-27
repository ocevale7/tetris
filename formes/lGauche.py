from .carres import Carre
from .forme import Forme

class LGauche(Forme):

    num = 4

    def __init__(self, couleur, orientation):

        super().__init__(couleur, orientation, [ 
                                    Carre(couleur, 540, 160),
                                    Carre(couleur, 540, 200),
                                    Carre(couleur, 540, 240),
                                    Carre(couleur, 500, 240)]
                        )
    
    def miseEnJeux(self):
        self.listeCarres[0].rect.x = 240
        self.listeCarres[0].rect.y = -80

        self.listeCarres[1].rect.x = 240
        self.listeCarres[1].rect.y = -40

        self.listeCarres[2].rect.x = 240
        self.listeCarres[2].rect.y = 0

        self.listeCarres[3].rect.x = 200
        self.listeCarres[3].rect.y = 0

        super().miseEnJeux()
