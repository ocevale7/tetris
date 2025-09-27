from .carres import Carre
from abc import ABC, abstractmethod
from math import cos, sin, pi
import pygame

class Forme(ABC):

    def __init__(self, couleur, orientation, listeCarres):
        self.couleur = couleur
        self.carresPygameGroup = pygame.sprite.Group()
        self.listeCarres = []
        self.orientation = orientation

        for carre in listeCarres:
            self.carresPygameGroup.add(carre)
            self.listeCarres.append(carre)

        self.miseEnJeux()

    def move(self, x, y):
        for carre in self.carresPygameGroup:
            carre.rect.x += x
            carre.rect.y += y
    
    def draw(self, screen):
        self.carresPygameGroup.draw(screen)

    def centre(self):
        somme_x = 0
        somme_y = 0
        for carre in self.listeCarres:
            somme_x += carre.rect.x
            somme_y += carre.rect.y
        
        return (int(somme_x / len(self.listeCarres)), int(somme_y / len(self.listeCarres)))
    
    def ajustePos(self, x_min_origin, y_min_origin, liste = None):

        if liste is None:

            x_min_new, y_min_new = self.listeCarres[0].rect.x, self.listeCarres[0].rect.y

            for carre in self.listeCarres:
                if carre.rect.x < x_min_new:
                    x_min_new = carre.rect.x
                if carre.rect.y < y_min_new:
                    y_min_new = carre.rect.y
            
            x_dist = x_min_new - x_min_origin
            y_dist = y_min_new - y_min_origin

            for carre in self.listeCarres:
                carre.rect.x -= x_dist
                carre.rect.y -= y_dist
        else:

            x_min_new, y_min_new = liste[0][0], liste[0][1]

            for carre in liste:
                if carre[0] < x_min_new:
                    x_min_new = carre[0]
                if carre[1] < y_min_new:
                    y_min_new = carre[1]
            
            x_dist = x_min_new - x_min_origin
            y_dist = y_min_new - y_min_origin

            for i in range(len(liste)):
                liste[i] = (liste[i][0] - x_dist, liste[i][1] - y_dist)

    def tourne(self):

        x_min_origin, y_min_origin = self.listeCarres[0].rect.x, self.listeCarres[0].rect.y

        for carre in self.listeCarres:
            if carre.rect.x < x_min_origin:
                x_min_origin = carre.rect.x
            if carre.rect.y < y_min_origin:
                y_min_origin = carre.rect.y

        cx, cy = self.centre()
        for carre in self.listeCarres:
            dx, dy = carre.rect.x - cx, carre.rect.y - cy
            dx_rot, dy_rot = -dy, dx
            carre.rect.x, carre.rect.y = dx_rot + cx, dy_rot + cy
        
        self.ajustePos(x_min_origin, y_min_origin)

    def resultsOfTourne(self):

        x_min_origin, y_min_origin = self.listeCarres[0].rect.x, self.listeCarres[0].rect.y

        for carre in self.listeCarres:
            if carre.rect.x < x_min_origin:
                x_min_origin = carre.rect.x
            if carre.rect.y < y_min_origin:
                y_min_origin = carre.rect.y

        l = []
        cx, cy = self.centre()

        for carre in self.listeCarres:
            dx, dy = carre.rect.x - cx, carre.rect.y - cy
            dx_rot, dy_rot = -dy, dx
            l.append((dx_rot + cx, dy_rot + cy))
        self.ajustePos(x_min_origin, y_min_origin, l)

        return l
    
    def miseEnJeux(self):

        for _ in range(self.orientation):
            self.tourne()
        
        y_max = self.listeCarres[0].rect.y

        for carre in self.listeCarres:
            if carre.rect.y > y_max:
                y_max = carre.rect.y
        
        for carre in self.listeCarres:
            carre.rect.y -= y_max
    
    def __str__(self):
        output = "Forme num " + str(self.num) + "\n"
        for carre in self.listeCarres:
            output += str(carre) + "\n"
        return output