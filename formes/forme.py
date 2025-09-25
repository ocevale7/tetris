from carres import Carre
from abc import ABC, abstractmethod
from math import cos,sin,pi
import pygame

class Forme(ABC):

    def __init__(self, couleur, listeCarres):
        self.couleur = couleur
        self.carresPygameGroup = pygame.sprite.Group()
        self.listeCarres = []
        for carre in listeCarres:
            self.carresPygameGroup.add(carre)
            self.listeCarres.append(carre)

    @abstractmethod
    def miseEnJeux(self):
        """ Déplace les carrées de la forme pour la mettre en jeux"""
        pass

    def centre(self):
        somme_x = 0
        somme_y = 0
        for carre in self.listeCarres:
            somme_x += carre.rect.x
            somme_y += carre.rect.y
        
        return (int(somme_x / len(self.listeCarres)), int(somme_y / len(self.listeCarres)))

    def tourne(self):
        cx, cy = self.centre()
        for carre in self.listeCarres:
            dx, dy = carre.rect.x - cx, carre.rect.y - cy
            dx_rot, dy_rot = -dy, dx
            carre.rect.x, carre.rect.y = dx_rot + cx, dy_rot + cy
    
    def __str__(self):
        output = ""
        for carre in self.listeCarres:
            output += str(carre) + "\n"
        return output