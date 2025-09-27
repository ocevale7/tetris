import pygame
from random import randint

from formes.carres import *
from formes.cube import Cube
from formes.long import Long
from formes.lDroite import LDroite
from formes.lGauche import LGauche
from formes.pont import Pont
from formes.eclaireDroit import EclaireDroit
from formes.eclaireGauche import EclaireGauche

class Game():

  all_formes = [Cube, Long, LDroite, LGauche, Pont, EclaireDroit, EclaireGauche]

  def __init__(self):

    self.acc = 10
    self.gravity_init = 2

    self.gravity = self.gravity_init

    self.points = 0
    self.n_piece = 0

    self.all_carres = pygame.sprite.Group()
    self.piece_en_jeu = None
    self.piece_en_attente = None

    self.nbCarreParLigne = {}
    for i in range(40, 840, 40):
      self.nbCarreParLigne[i] = 0

  def check_collision_foot(self,group_1,group_2):

    for sprite in group_1:

      sprite_x = (sprite.rect.x,sprite.rect.x+sprite.width)
      sprite_y = (sprite.rect.y,sprite.rect.y+sprite.height)
      
      for entity in group_2:
          
        entity_x = (entity.rect.x,entity.rect.x+entity.width)
        entity_y = (entity.rect.y,entity.rect.y+entity.height)

        if (entity_x[0]<sprite_x[1]<=entity_x[1] or entity_x[0]<=sprite_x[0]<entity_x[1] or entity_x[0]<=(sprite_x[0]+sprite_x[1])/2<entity_x[1]) and entity_y[0] <= sprite_y[1] <= entity_y[1]:
          return True

    return False

  def check_collision_right(self, group_1,group_2):

    for sprite in group_1:
    
      sprite_x = (sprite.rect.x,sprite.rect.x+sprite.width)
      sprite_y = (sprite.rect.y,sprite.rect.y+sprite.height)
      
      for entity in group_2:
          
        entity_x = (entity.rect.x,entity.rect.x+entity.width)
        entity_y = (entity.rect.y,entity.rect.y+entity.height)

        if entity_x[0]<=sprite_x[1]<=entity_x[1] and (entity_y[0] <= sprite_y[0] < entity_y[1] or entity_y[0] < sprite_y[1] <= entity_y[1] or entity_y[0] < (sprite_y[0]+sprite_y[1])/2 <= entity_y[1]):
          return True

    return False

  def check_collision_left(self, group_1,group_2):

    for sprite in group_1:
    
      sprite_x = (sprite.rect.x,sprite.rect.x+sprite.width)
      sprite_y = (sprite.rect.y,sprite.rect.y+sprite.height)

      for entity in group_2:

        entity_x = (entity.rect.x,entity.rect.x+entity.width)
        entity_y = (entity.rect.y,entity.rect.y+entity.height)

        if entity_x[0]<=sprite_x[0]<=entity_x[1] and (entity_y[0] <= sprite_y[0] < entity_y[1] or entity_y[0] < sprite_y[1] <= entity_y[1] or entity_y[0] < (sprite_y[0]+sprite_y[1])/2 <= entity_y[1]):
          return True
          
    return False

  def new_piece(self):

    self.n_piece += 1

    if self.n_piece == 1 :

      self.n_piece += 1

      orientation = randint(0,3)
      couleur = randint(0,4)
      self.piece_en_jeu = self.all_formes[randint(0, 6)](couleur, orientation)
      self.piece_en_jeu.miseEnJeux()
    
    orientation = randint(0,3)
    couleur = randint(0,4)
    self.piece_en_attente = self.all_formes[randint(0, 6)](couleur, orientation)
      

  def ligne(self):
    lignesASuppr = []
    for i in range(40, 840, 40):
      if self.nbCarreParLigne[i] == 10:
        lignesASuppr.append(i)
        self.nbCarreParLigne[i] = 0
    
    for carre in self.all_carres:
      if carre.rect.y in lignesASuppr:
        self.all_carres.remove(carre)
    print(lignesASuppr)
    for carre in self.all_carres:
      for ligneSuppr in lignesASuppr:
        if carre.rect.y < ligneSuppr:
          carre.rect.y += 40
        
              
  def relunch(self):
    pygameGroupe = self.piece_en_jeu.carresPygameGroup
    bon = True
    for carre in self.piece_en_jeu.listeCarres:
      if carre.rect.y > 800:
        bon = False
        break
    if not(bon) or self.check_collision_foot(pygameGroupe,self.all_carres):
      for carre in pygameGroupe:
        carre.rect.y = round(carre.rect.y / 40) * 40
        self.nbCarreParLigne[carre.rect.y] += 1
        self.all_carres.add(carre)
      self.ligne()
      self.piece_en_jeu = self.piece_en_attente
      self.new_piece()
      self.gravity = self.gravity_init

  def lose(self):
    for i in self.all_carres:
      if i.rect.y <= 0:
        return True
    return False
              

        
        
