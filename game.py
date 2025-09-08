import pygame
from carres import *
from random import randint

class Game():

    def __init__(self):

        self.acc = 10
        self.gravity_init = 2

        self.end = False

        self.gravity = self.gravity_init

        self.pos = 0
        self.pos_act = 0
        self.forme = 0
        self.forme_act = 0
        self.couleur = 0

        self.piece_copie = 0

        self.points = 0
        self.n_piece = 0

        self.all_carres = pygame.sprite.Group()
        self.all_carres_move = pygame.sprite.Group()
        self.all_carres_att = pygame.sprite.Group()

        self.all_fond = pygame.sprite.Group()

        self.ensemble_carre = [("carre_1_x","carre_1_y"),
                               ("carre_2_x","carre_2_y"),
                               ("carre_3_x","carre_3_y"),
                               ("carre_4_x","carre_4_y")]

        self.position = {"x" : 0,
                         "y" : 0}

        self.cube_att = [{ "carre_1_x" : 500,
                      "carre_1_y" : 180,

                      "carre_2_x" : 540,
                      "carre_2_y" : 180,

                      "carre_3_x" : 500,
                      "carre_3_y" : 220,

                      "carre_4_x" : 540,
                      "carre_4_y" : 220},

                     { "carre_1_x" : 500,
                      "carre_1_y" : 180,

                      "carre_2_x" : 540,
                      "carre_2_y" : 180,

                      "carre_3_x" : 500,
                      "carre_3_y" : 220,

                      "carre_4_x" : 540,
                      "carre_4_y" : 220},

                     { "carre_1_x" : 500,
                      "carre_1_y" : 180,

                      "carre_2_x" : 540,
                      "carre_2_y" : 180,

                      "carre_3_x" : 500,
                      "carre_3_y" : 220,

                      "carre_4_x" : 540,
                      "carre_4_y" : 220},

                     { "carre_1_x" : 500,
                      "carre_1_y" : 180,

                      "carre_2_x" : 540,
                      "carre_2_y" : 180,

                      "carre_3_x" : 500,
                      "carre_3_y" : 220,

                      "carre_4_x" : 540,
                      "carre_4_y" : 220}]

        self.long_att = [{ "carre_1_x" : 460,
                       "carre_1_y" : 200,

                       "carre_2_x" : 500,
                       "carre_2_y" : 200,

                       "carre_3_x" : 540,
                       "carre_3_y" : 200,

                       "carre_4_x" : 580,
                       "carre_4_y" : 200},

                     { "carre_1_x" : 520,
                       "carre_1_y" : 140,

                       "carre_2_x" : 520,
                       "carre_2_y" : 180,

                       "carre_3_x" : 520,
                       "carre_3_y" : 220,

                       "carre_4_x" : 520,
                       "carre_4_y" : 260},

                     { "carre_1_x" : 460,
                       "carre_1_y" : 200,

                       "carre_2_x" : 500,
                       "carre_2_y" : 200,

                       "carre_3_x" : 540,
                       "carre_3_y" : 200,

                       "carre_4_x" : 580,
                       "carre_4_y" : 200},

                     { "carre_1_x" : 520,
                       "carre_1_y" : 140,

                       "carre_2_x" : 520,
                       "carre_2_y" : 180,

                       "carre_3_x" : 520,
                       "carre_3_y" : 220,

                       "carre_4_x" : 520,
                       "carre_4_y" : 260}]

        self.L_d_att = [{ "carre_1_x" : 500,
                    "carre_1_y" : 160,

                    "carre_2_x" : 500,
                    "carre_2_y" : 200,

                    "carre_3_x" : 500,
                    "carre_3_y" : 240,

                    "carre_4_x" : 540,
                    "carre_4_y" : 240},

                    { "carre_1_x" : 560,
                    "carre_1_y" : 180,

                    "carre_2_x" : 520,
                    "carre_2_y" : 180,

                    "carre_3_x" : 480,
                    "carre_3_y" : 180,

                    "carre_4_x" : 480,
                    "carre_4_y" : 220},

                    { "carre_1_x" : 540,
                    "carre_1_y" : 240,

                    "carre_2_x" : 540,
                    "carre_2_y" : 200,

                    "carre_3_x" : 540,
                    "carre_3_y" : 160,

                    "carre_4_x" : 500,
                    "carre_4_y" : 160},

                  { "carre_1_x" : 480,
                    "carre_1_y" : 220,

                    "carre_2_x" : 520,
                    "carre_2_y" : 220,

                    "carre_3_x" : 560,
                    "carre_3_y" : 220,

                    "carre_4_x" : 560,
                    "carre_4_y" : 180}]

        self.L_g_att = [{ "carre_1_x" : 540,
                    "carre_1_y" : 160,

                    "carre_2_x" : 540,
                    "carre_2_y" : 200,

                    "carre_3_x" : 540,
                    "carre_3_y" : 240,

                    "carre_4_x" : 500,
                    "carre_4_y" : 240},

                    { "carre_1_x" : 560,
                    "carre_1_y" : 220,

                    "carre_2_x" : 520,
                    "carre_2_y" : 220,

                    "carre_3_x" : 480,
                    "carre_3_y" : 220,

                    "carre_4_x" : 480,
                    "carre_4_y" : 180},

                    { "carre_1_x" : 500,
                    "carre_1_y" : 240,

                    "carre_2_x" : 500,
                    "carre_2_y" : 200,

                    "carre_3_x" : 500,
                    "carre_3_y" : 160,

                    "carre_4_x" : 540,
                    "carre_4_y" : 160},

                  { "carre_1_x" : 480,
                    "carre_1_y" : 180,

                    "carre_2_x" : 520,
                    "carre_2_y" : 180,

                    "carre_3_x" : 560,
                    "carre_3_y" : 180,

                    "carre_4_x" : 560,
                    "carre_4_y" : 220}]

        self.pont_att = [{ "carre_1_x" : 480,
                       "carre_1_y" : 220,

                       "carre_2_x" : 520,
                       "carre_2_y" : 220,

                       "carre_3_x" : 520,
                       "carre_3_y" : 180,

                       "carre_4_x" : 560,
                       "carre_4_y" : 220},

                     { "carre_1_x" : 500,
                       "carre_1_y" : 160,

                       "carre_2_x" : 500,
                       "carre_2_y" : 200,

                       "carre_3_x" : 540,
                       "carre_3_y" : 200,

                       "carre_4_x" : 500,
                       "carre_4_y" : 240},

                     { "carre_1_x" : 560,
                       "carre_1_y" : 180,

                       "carre_2_x" : 520,
                       "carre_2_y" : 180,

                       "carre_3_x" : 520,
                       "carre_3_y" : 220,

                       "carre_4_x" : 480,
                       "carre_4_y" : 180},

                     { "carre_1_x" : 540,
                       "carre_1_y" : 240,

                       "carre_2_x" : 540,
                       "carre_2_y" : 200,

                       "carre_3_x" : 500,
                       "carre_3_y" : 200,

                       "carre_4_x" : 540,
                       "carre_4_y" : 160}]

        self.eclair_d_att = [{"carre_1_x" : 500,
                        "carre_1_y" : 240,

                        "carre_2_x" : 500,
                        "carre_2_y" : 200,

                        "carre_3_x" : 540,
                        "carre_3_y" : 200,

                        "carre_4_x" : 540,
                        "carre_4_y" : 160},

                         {"carre_1_x" : 480,
                        "carre_1_y" : 180,

                        "carre_2_x" : 520,
                        "carre_2_y" : 180,

                        "carre_3_x" : 520,
                        "carre_3_y" : 220,

                        "carre_4_x" : 560,
                        "carre_4_y" : 220},

                         {"carre_1_x" : 500,
                        "carre_1_y" : 240,

                        "carre_2_x" : 500,
                        "carre_2_y" : 200,

                        "carre_3_x" : 540,
                        "carre_3_y" : 200,

                        "carre_4_x" : 540,
                        "carre_4_y" : 160},

                         {"carre_1_x" : 480,
                        "carre_1_y" : 180,

                        "carre_2_x" : 520,
                        "carre_2_y" : 180,

                        "carre_3_x" : 520,
                        "carre_3_y" : 220,

                        "carre_4_x" : 560,
                        "carre_4_y" : 220}]

        self.eclair_g_att = [{"carre_1_x" : 540,
                        "carre_1_y" : 240,

                        "carre_2_x" : 540,
                        "carre_2_y" : 200,

                        "carre_3_x" : 500,
                        "carre_3_y" : 200,

                        "carre_4_x" : 500,
                        "carre_4_y" : 160},

                         {"carre_1_x" : 560,
                        "carre_1_y" : 180,

                        "carre_2_x" : 520,
                        "carre_2_y" : 180,

                        "carre_3_x" : 520,
                        "carre_3_y" : 220,

                        "carre_4_x" : 480,
                        "carre_4_y" : 220},

                         {"carre_1_x" : 540,
                        "carre_1_y" : 240,

                        "carre_2_x" : 540,
                        "carre_2_y" : 200,

                        "carre_3_x" : 500,
                        "carre_3_y" : 200,

                        "carre_4_x" : 500,
                        "carre_4_y" : 160},

                         {"carre_1_x" : 560,
                        "carre_1_y" : 180,

                        "carre_2_x" : 520,
                        "carre_2_y" : 180,

                        "carre_3_x" : 520,
                        "carre_3_y" : 220,

                        "carre_4_x" : 480,
                        "carre_4_y" : 220}]

        self.cube = [{ "carre_1_x" : 200,
                      "carre_1_y" : -40,

                      "carre_2_x" : 240,
                      "carre_2_y" : -40,

                      "carre_3_x" : 200,
                      "carre_3_y" : 0,

                      "carre_4_x" : 240,
                      "carre_4_y" : 0},

                     { "carre_1_x" : 200,
                      "carre_1_y" : -40,

                      "carre_2_x" : 240,
                      "carre_2_y" : -40,

                      "carre_3_x" : 200,
                      "carre_3_y" : 0,

                      "carre_4_x" : 240,
                      "carre_4_y" : 0},

                     { "carre_1_x" : 200,
                      "carre_1_y" : -40,

                      "carre_2_x" : 240,
                      "carre_2_y" : -40,

                      "carre_3_x" : 200,
                      "carre_3_y" : 0,

                      "carre_4_x" : 240,
                      "carre_4_y" : 0},

                     { "carre_1_x" : 200,
                      "carre_1_y" : -40,

                      "carre_2_x" : 240,
                      "carre_2_y" : -40,

                      "carre_3_x" : 200,
                      "carre_3_y" : 0,

                      "carre_4_x" : 240,
                      "carre_4_y" : 0}]

        

        self.long = [{ "carre_1_x" : 160,
                       "carre_1_y" : 0,

                       "carre_2_x" : 200,
                       "carre_2_y" : 0,

                       "carre_3_x" : 240,
                       "carre_3_y" : 0,

                       "carre_4_x" : 280,
                       "carre_4_y" : 0},

                     { "carre_1_x" : 240,
                       "carre_1_y" : -120,

                       "carre_2_x" : 240,
                       "carre_2_y" : -80,

                       "carre_3_x" : 240,
                       "carre_3_y" : -40,

                       "carre_4_x" : 240,
                       "carre_4_y" : 0},

                     { "carre_1_x" : 160,
                       "carre_1_y" : 0,

                       "carre_2_x" : 200,
                       "carre_2_y" : 0,

                       "carre_3_x" : 240,
                       "carre_3_y" : 0,

                       "carre_4_x" : 280,
                       "carre_4_y" : 0},

                     { "carre_1_x" : 240,
                       "carre_1_y" : -120,

                       "carre_2_x" : 240,
                       "carre_2_y" : -80,

                       "carre_3_x" : 240,
                       "carre_3_y" : -40,

                       "carre_4_x" : 240,
                       "carre_4_y" : 0}]

        self.L_d = [{ "carre_1_x" : 200,
                    "carre_1_y" : -80,

                    "carre_2_x" : 200,
                    "carre_2_y" : -40,

                    "carre_3_x" : 200,
                    "carre_3_y" : 0,

                    "carre_4_x" : 240,
                    "carre_4_y" : 0},

                    { "carre_1_x" : 280,
                    "carre_1_y" : -40,

                    "carre_2_x" : 240,
                    "carre_2_y" : -40,

                    "carre_3_x" : 200,
                    "carre_3_y" : -40,

                    "carre_4_x" : 200,
                    "carre_4_y" : 0},

                    { "carre_1_x" : 240,
                    "carre_1_y" : 0,

                    "carre_2_x" : 240,
                    "carre_2_y" : -40,

                    "carre_3_x" : 240,
                    "carre_3_y" : -80,

                    "carre_4_x" : 200,
                    "carre_4_y" : -80},

                  { "carre_1_x" : 200,
                    "carre_1_y" : 0,

                    "carre_2_x" : 240,
                    "carre_2_y" : 0,

                    "carre_3_x" : 280,
                    "carre_3_y" : 0,

                    "carre_4_x" : 280,
                    "carre_4_y" : -40}]

        self.L_g = [{ "carre_1_x" : 240,
                    "carre_1_y" : -80,

                    "carre_2_x" : 240,
                    "carre_2_y" : -40,

                    "carre_3_x" : 240,
                    "carre_3_y" : 0,

                    "carre_4_x" : 200,
                    "carre_4_y" : 0},

                    { "carre_1_x" : 280,
                    "carre_1_y" : 0,

                    "carre_2_x" : 240,
                    "carre_2_y" : 0,

                    "carre_3_x" : 200,
                    "carre_3_y" : 0,

                    "carre_4_x" : 200,
                    "carre_4_y" : -40},

                    { "carre_1_x" : 200,
                    "carre_1_y" : 0,

                    "carre_2_x" : 200,
                    "carre_2_y" : -40,

                    "carre_3_x" : 200,
                    "carre_3_y" : -80,

                    "carre_4_x" : 240,
                    "carre_4_y" : -80},

                  { "carre_1_x" : 200,
                    "carre_1_y" : -40,

                    "carre_2_x" : 240,
                    "carre_2_y" : -40,

                    "carre_3_x" : 280,
                    "carre_3_y" : -40,

                    "carre_4_x" : 280,
                    "carre_4_y" : 0}]

        self.pont = [{ "carre_1_x" : 200,
                       "carre_1_y" : 0,

                       "carre_2_x" : 240,
                       "carre_2_y" : 0,

                       "carre_3_x" : 240,
                       "carre_3_y" : -40,

                       "carre_4_x" : 280,
                       "carre_4_y" : 0},

                     { "carre_1_x" : 200,
                       "carre_1_y" : -80,

                       "carre_2_x" : 200,
                       "carre_2_y" : -40,

                       "carre_3_x" : 240,
                       "carre_3_y" : -40,

                       "carre_4_x" : 200,
                       "carre_4_y" : 0},

                     { "carre_1_x" : 280,
                       "carre_1_y" : -40,

                       "carre_2_x" : 240,
                       "carre_2_y" : -40,

                       "carre_3_x" : 240,
                       "carre_3_y" : 0,

                       "carre_4_x" : 200,
                       "carre_4_y" : -40},

                     { "carre_1_x" : 240,
                       "carre_1_y" : 0,

                       "carre_2_x" : 240,
                       "carre_2_y" : -40,

                       "carre_3_x" : 200,
                       "carre_3_y" : -40,

                       "carre_4_x" : 240,
                       "carre_4_y" : -80}]

        self.eclair_d = [{"carre_1_x" : 240,
                        "carre_1_y" : -80,

                        "carre_2_x" : 240,
                        "carre_2_y" : -40,

                        "carre_3_x" : 200,
                        "carre_3_y" : -40,

                        "carre_4_x" : 200,
                        "carre_4_y" : 0},

                         {"carre_1_x" : 280,
                        "carre_1_y" : 0,

                        "carre_2_x" : 240,
                        "carre_2_y" : 0,

                        "carre_3_x" : 240,
                        "carre_3_y" : -40,

                        "carre_4_x" : 200,
                        "carre_4_y" : -40},

                         {"carre_1_x" : 240,
                        "carre_1_y" : -80,

                        "carre_2_x" : 240,
                        "carre_2_y" : -40,

                        "carre_3_x" : 200,
                        "carre_3_y" : -40,

                        "carre_4_x" : 200,
                        "carre_4_y" : 0},

                         {"carre_1_x" : 280,
                        "carre_1_y" : 0,

                        "carre_2_x" : 240,
                        "carre_2_y" : 0,

                        "carre_3_x" : 240,
                        "carre_3_y" : -40,

                        "carre_4_x" : 200,
                        "carre_4_y" : -40}]

        self.eclair_g = [{"carre_1_x" : 200,
                        "carre_1_y" : -80,

                        "carre_2_x" : 200,
                        "carre_2_y" : -40,

                        "carre_3_x" : 240,
                        "carre_3_y" : -40,

                        "carre_4_x" : 240,
                        "carre_4_y" : 0},

                         {"carre_1_x" : 280,
                        "carre_1_y" : -40,

                        "carre_2_x" : 240,
                        "carre_2_y" : -40,

                        "carre_3_x" : 240,
                        "carre_3_y" : 0,

                        "carre_4_x" : 200,
                        "carre_4_y" : 0},

                         {"carre_1_x" : 200,
                        "carre_1_y" : -80,

                        "carre_2_x" : 200,
                        "carre_2_y" : -40,

                        "carre_3_x" : 240,
                        "carre_3_y" : -40,

                        "carre_4_x" : 240,
                        "carre_4_y" : 0},

                         {"carre_1_x" : 280,
                        "carre_1_y" : -40,

                        "carre_2_x" : 240,
                        "carre_2_y" : -40,

                        "carre_3_x" : 240,
                        "carre_3_y" : 0,

                        "carre_4_x" : 200,
                        "carre_4_y" : 0}]

        self.Dico_pieces = { 1 : self.cube,
                        2 : self.long,
                        3 : self.L_d,
                        4 : self.L_g,
                        5 : self.pont,
                        6 : self.eclair_d,
                        7 : self.eclair_g}

        self.Dico_pieces_att = { 1 : self.cube_att,
                        2 : self.long_att,
                        3 : self.L_d_att,
                        4 : self.L_g_att,
                        5 : self.pont_att,
                        6 : self.eclair_d_att,
                        7 : self.eclair_g_att}

    def carres_move_launch(self,couleur):
        self.all_carres_move.add(carre(self,couleur))

    def  carres_launch(self,couleur):
        self.all_carres.add(carre(self,couleur))

    def  carres_att_launch(self,couleur):
        self.all_carres_att.add(carre(self,couleur))

    def  fond_launch(self,x,y):
        self.all_fond.add(fond(self,x,y))

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

            self.pos_act = randint(0,3)
            self.forme_act = randint(1,7)
            self.couleur = randint(0,4)

            fo = self.Dico_pieces[self.forme_act]

            self.piece_copie = self.Dico_pieces[self.forme_act]

            for car in self.ensemble_carre:
                self.position["x"] = fo[self.pos_act][car[0]]
                self.position["y"] = fo[self.pos_act][car[1]]
                self.carres_move_launch(self.couleur)

        self.pos = randint(0,3)
        self.forme = randint(1,7)
        self.couleur = randint(0,4)

        fo = self.Dico_pieces_att[self.forme]

        for car in self.ensemble_carre:
            self.position["x"] = fo[self.pos][car[0]]
            self.position["y"] = fo[self.pos][car[1]]
            self.carres_att_launch(self.couleur)

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
                self.end = True

        return self.end
                

        
        
