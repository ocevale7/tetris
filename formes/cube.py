from .carres import Carre
from .forme import Forme

class Cube(Forme):

    num = 1

    def __init__(self, couleur, orientation):

        self.matrix = [
            [1, 1],
            [1, 1]
        ]

        super().__init__(couleur, orientation)
