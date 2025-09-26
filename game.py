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
    self.all_fond = pygame.sprite.Group()
    self.piece_en_jeu = None
    self.piece_en_attente = None

  def carres_move_launch(self,couleur):
    self.all_carres_move.add(Carre(self,couleur))

  def carres_launch(self,couleur):
    self.all_carres.add(Carre(self,couleur))

  def carres_att_launch(self,couleur):
    self.all_carres_att.add(Carre(self,couleur))

  def fond_launch(self,x,y):
    self.all_fond.add(Fond(self,x,y))

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

      for entity in group_2:fo = self.Dico_pieces[self.forme_act]

          self.piece_copie = self.Dico_pieces[self.forme_act]
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

      pos = {}
      supr = 0
      n_supr = {}
      
      for i in self.all_carres:
          y = i.rect.y
          if pos.get(y) != None:
              pos[y] += 1
          else :
              pos[y] = 1
      
      supr = [i for i in pos if pos[i] == 10]

      for elt in range(len(supr)):
          
          [i.remove("stat") for i in self.all_carres if i.rect.y == supr[elt]]

          self.points += 100 * (elt+1)

          for i in self.all_carres:
              if i.rect.y < supr[elt]:
                  y = i
                  if n_supr.get(y) != None:
                      n_supr[y] += 40
                  else :
                      n_supr[y] = 40
                      
      for i in n_supr:
          i.rect.y += n_supr[i]

  def echange(self):

      fo = self.Dico_pieces[self.forme]

      self.forme_act = self.forme
      self.pos_act = self.pos

      self.piece_copie = self.Dico_pieces[self.forme_act]

      for car in self.ensemble_carre:
              self.position["x"] = fo[self.pos_act][car[0]]
              self.position["y"] = fo[self.pos_act][car[1]]
              self.carres_move_launch(self.couleur)

      for i in self.all_carres_att:
          i.remove("att")
              
  def relunch(self):
    for i in self.all_carres_move:
      if self.check_collision_foot(self.all_carres_move,self.all_carres) or self.check_collision_foot(self.all_carres_move,self.all_fond):
        for i in self.all_carres_move:
          self.position["x"] = i.rect.x
          self.position["y"] = (i.rect.y//40)*40
          self.carres_launch(i.couleur)
          i.remove("move")
        self.ligne()
        self.echange()
        self.new_piece()
        self.gravity = self.gravity_init

  def lose(self):
    for i in self.all_carres:
      if i.rect.y <= 0:
        return True
    return False
              

        
        
