import pygame
import time

from game import Game
from carres import *
from math import sqrt

game = Game()
carre = carre(game,0)

pygame.init()

pygame.display.set_caption("Tetris")
screen = pygame.display.set_mode((640,880))

running = True
background = pygame.image.load('assets/bg.png')

font = pygame.font.Font(None,50)

pygame.mixer.music.load('assets/sounds/tetris.mp3')
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play()

game.new_piece()

for i in range(40,440,40):
    game.fond_launch(i,840)

while running:

    if pygame.mixer.music.get_pos() > 103000:
                pygame.mixer.music.pause()
                pygame.mixer.music.load('assets/sounds/tetris.mp3')
                pygame.mixer.music.play()

    screen.blit(background,(0,0))
    game.all_fond.draw(screen)

    texte = font.render(str(game.points),1,(0,0,0))
    screen.blit(texte,(520,485))
    
    for i in game.all_carres_move:
        i.rect.y += game.gravity

    for i in range(0,4):
        carre = -1
        for y in range(0,4):
            carre += 1
            #game.piece_copie[i][game.ensemble_carre[carre][1]] += game.gravity
        

    game.all_carres_move.draw(screen)
    game.all_carres.draw(screen)
    game.all_carres_att.draw(screen)

    game.relunch()

    if game.lose():
        running = False

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                pygame.quit()
            elif event.key == pygame.K_d:
                bon = True
                for i in game.all_carres_move:
                    if i.rect.x >= 400 or game.check_collision_right(game.all_carres_move,game.all_carres):
                        bon = False
                if bon:
                    for i in game.all_carres_move:
                        i.rect.x += 40
                        
            elif event.key == pygame.K_q:
                bon = True
                for i in game.all_carres_move:
                    if i.rect.x <= 40 or game.check_collision_left(game.all_carres_move,game.all_carres):
                        bon = False
                if bon:
                    for i in game.all_carres_move:
                        i.rect.x -= 40

            elif event.key == pygame.K_z:

                game.pos_act = (game.pos_act + 1) % 4

                anc_pos_x_min = 640
                anc_pos_y_min = 880

                new_pos_x_min = 640
                new_pos_y_min = 880

                for i in game.all_carres_move:
                    if i.rect.x <= anc_pos_x_min:
                        anc_pos_x_min = i.rect.x
                    if i.rect.y <= anc_pos_y_min:
                        anc_pos_y_min = i.rect.y
                
                for carre in range(4):
                    pos_dep_x = game.Dico_pieces[game.forme_act][game.pos_act][game.ensemble_carre[carre][0]]
                    pos_dep_y = game.Dico_pieces[game.forme_act][game.pos_act][game.ensemble_carre[carre][1]]

                    if pos_dep_x <= new_pos_x_min:
                        new_pos_x_min = pos_dep_x
                    if pos_dep_y <= new_pos_y_min:
                        new_pos_y_min = pos_dep_y

                dist_x = sqrt((anc_pos_x_min-new_pos_x_min)**2)
                dist_y = sqrt((anc_pos_y_min-new_pos_y_min)**2)

                carre = -1

                for i in game.all_carres_move:

                    carre += 1

                    pos_dep_x = game.Dico_pieces[game.forme_act][game.pos_act][game.ensemble_carre[carre][0]]
                    pos_dep_y = game.Dico_pieces[game.forme_act][game.pos_act][game.ensemble_carre[carre][1]]

                    i.rect.x = pos_dep_x + dist_x
                    i.rect.y = pos_dep_y + dist_y


                    

            elif event.key == pygame.K_s:
                game.gravity = game.acc

            
