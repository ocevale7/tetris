from carres import Carre
from forme import Forme

class Pont(Forme):

    num = 5

    def __init__(self, couleur, orientation):

        super().__init__(couleur, orientation, [ 
                                    Carre(couleur, 480, 220),
                                    Carre(couleur, 520, 220),
                                    Carre(couleur, 520, 180),
                                    Carre(couleur, 560, 220)]
                        )
    
    def miseEnJeux(self):
        self.listeCarres[0].rect.x = 200
        self.listeCarres[0].rect.y = 0

        self.listeCarres[1].rect.x = 240
        self.listeCarres[1].rect.y = 0

        self.listeCarres[2].rect.x = 240
        self.listeCarres[2].rect.y = -40

        self.listeCarres[3].rect.x = 280
        self.listeCarres[3].rect.y = 0

        for _ in range self.orientation:
            self.tourne()
