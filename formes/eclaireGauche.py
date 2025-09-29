from .carres import Carre
from .forme import Forme

class EclaireGauche(Forme):

    num = 7

    def __init__(self, couleur, orientation):

        self.matrix = [
            [0, 1, 0],
            [1, 1, 0],
            [1, 0, 0]
        ]

        super().__init__(couleur, orientation)