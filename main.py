import pygame
import time

from game import Game

game = Game()
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

while running:

    if pygame.mixer.music.get_pos() > 103000:
                pygame.mixer.music.pause()
                pygame.mixer.music.load('assets/sounds/tetris.mp3')
                pygame.mixer.music.play()

    screen.blit(background,(0,0))

    texte = font.render(str(game.points),1,(0,0,0))
    screen.blit(texte,(520,485))
    
    game.piece_en_jeu.move(0, game.gravity)

    game.piece_en_jeu.draw(screen)
    game.all_carres.draw(screen)
    game.piece_en_attente.draw(screen)

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
                for carre in game.piece_en_jeu.carresPygameGroup:
                    if carre.rect.x >= 400:
                        bon = False
                        break
                if bon and not(game.check_collision_right(game.piece_en_jeu.carresPygameGroup, game.all_carres)):
                    game.piece_en_jeu.move(40, 0)
                        
            elif event.key == pygame.K_q:
                bon = True
                for carre in game.piece_en_jeu.carresPygameGroup:
                    if carre.rect.x <= 40:
                        bon = False
                        break
                if bon and not(game.check_collision_left(game.piece_en_jeu.carresPygameGroup, game.all_carres)):
                    game.piece_en_jeu.move(-40, 0)

            elif event.key == pygame.K_z:
                bon = True
                l = game.piece_en_jeu.resultsOfTourne()
                for carre in l:
                    if carre[0] <= 0 or carre[0] >= 400 or carre[1] >= 840:
                        bon = False
                        break
                if bon:
                    game.piece_en_jeu.tourne()
                    
            elif event.key == pygame.K_s:
                game.gravity = game.acc

            
