import pygame

class carre(pygame.sprite.Sprite):

    def __init__(self,game,couleur):
        super().__init__()
        self.game = game

        self.couleur = couleur
        self.rouge = pygame.image.load('assets/carre_rouge.png')
        self.jaune = pygame.image.load('assets/carre_jaune.png')
        self.bleu = pygame.image.load('assets/carre_bleu.png')
        self.vert = pygame.image.load('assets/carre_vert.png')
        self.rose = pygame.image.load('assets/carre_rose.png')

        self.all_couleurs = [self.rouge,self.jaune,self.bleu,self.vert,self.rose]

        self.image = self.all_couleurs[self.couleur]
        
        self.rect = self.image.get_rect()
        self.rect.x = self.game.position["x"]
        self.rect.y = self.game.position["y"]
        self.width = self.image.get_rect()[2]
        self.height = self.image.get_rect()[3]

    def remove(self,groupe):
        if groupe == "move":
            self.game.all_carres_move.remove(self)
        elif groupe == "stat":
            self.game.all_carres.remove(self)
        elif groupe == "att":
            self.game.all_carres_att.remove(self)

class fond(pygame.sprite.Sprite):

    def __init__(self,game,x,y):
        super().__init__()
        self.game = game
        self.image = pygame.image.load('assets/fond.png')
        self.rect = self.image.get_rect()
        
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_rect()[2]
        self.height = self.image.get_rect()[3]

    def remove(self):
        self.game.all_carres_move.remove(self)
