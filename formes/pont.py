from .carres import Carre
from .forme import Forme

class Pont(Forme):

    num = 5

    def __init__(self, couleur, orientation):

        self.matrix = [
            [0, 1, 0],
            [1, 1, 1],
            [0, 0, 0]
        ]

        super().__init__(couleur, orientation, 480, 180)
