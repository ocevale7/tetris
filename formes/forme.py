from .carres import Carre
from abc import ABC, abstractmethod
from math import cos, sin, pi
import pygame

class Forme(ABC):

    depart = (460, 140)

    def __init__(self, couleur, orientation):

        self.couleur = couleur
        self.carresPygameGroup = pygame.sprite.Group()
        self.listeCarres = []
        self.orientation = orientation

        self.x = self.depart[0]
        self.y = self.depart[1]

        for _ in range(orientation):
            self.matrix = [list(row) for row in zip(*self.matrix)][::-1]

        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == 1:
                    newCarre = Carre(self.couleur, self.x + i*40, self.y + j*40)
                    self.carresPygameGroup.add(newCarre)
                    self.listeCarres.append(newCarre)
        
    
    def placeCarre(self, x, y):
        carreNb = 0
        self.x = x
        self.y = y
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == 1:
                    carre = self.listeCarres[carreNb]
                    carreNb += 1
                    carre.rect.x = x + i*40
                    carre.rect.y = y + j*40     

    def move(self, x, y):
        self.x += x
        self.y += y
        for carre in self.carresPygameGroup:
            carre.rect.x += x
            carre.rect.y += y
    
    def draw(self, screen):
        self.carresPygameGroup.draw(screen)

    def rotate(self, game):

        ancienneMatrix = self.matrix
        self.matrix = [list(row) for row in zip(*self.matrix)][::-1]
        self.placeCarre(self.x, self.y)

        bon = True
        for carre in game.piece_en_jeu.carresPygameGroup:
            if carre.rect.x >= 400 or carre.rect.x <= 40:
                bon = False
                break

        if not(bon) or game.check_collision_left(game.piece_en_jeu.carresPygameGroup, game.all_carres) or game.check_collision_right(game.piece_en_jeu.carresPygameGroup, game.all_carres) or game.check_collision_foot(game.piece_en_jeu.carresPygameGroup, game.all_carres) :
            self.matrix = ancienneMatrix
            self.placeCarre(self.x, self.y)
    
    def miseEnJeux(self, game):
        self.placeCarre(200, -80)
    
    def __str__(self):
        output = "Forme num " + str(self.num) + "\n"
        for carre in self.listeCarres:
            output += str(carre) + "\n"
        return output