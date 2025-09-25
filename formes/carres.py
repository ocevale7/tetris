import pygame

class Carre(pygame.sprite.Sprite):

    def __init__(self, game, couleur, x, y):
        super().__init__()
        self.game = game

        self.couleur = couleur
        self.rouge = pygame.image.load('../assets/carre_rouge.png')
        self.jaune = pygame.image.load('../assets/carre_jaune.png')
        self.bleu = pygame.image.load('../assets/carre_bleu.png')
        self.vert = pygame.image.load('../assets/carre_vert.png')
        self.rose = pygame.image.load('../assets/carre_rose.png')

        self.all_couleurs = [self.rouge,self.jaune,self.bleu,self.vert,self.rose]

        self.image = self.all_couleurs[self.couleur]
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_rect()[2]
        self.height = self.image.get_rect()[3]
    
    def __str__(self):
        return "Carre : (" + str(self.rect.x) + ", " + str(self.rect.y) + ")"

class Fond(pygame.sprite.Sprite):

    def __init__(self,game,x,y):
        super().__init__()
        self.game = game
        self.image = pygame.image.load('../assets/fond.png')
        self.rect = self.image.get_rect()
        
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_rect()[2]
        self.height = self.image.get_rect()[3]
