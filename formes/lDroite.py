from .carres import Carre
from .forme import Forme

class LDroite(Forme):

    num = 3

    def __init__(self, couleur, orientation):

        self.matrix = [
            [0, 1, 0],
            [0, 1, 0],
            [0, 1, 1]
        ]

        super().__init__(couleur, orientation, 500, 160)
