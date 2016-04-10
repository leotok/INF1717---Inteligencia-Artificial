import os, sys
import pygame
from pygame import display,movie
from helpers import *
from pygame.locals import *
from collections import deque

from plane import *
from tile import *
from AStar import *

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

# Main:

class Main(object):

    def __init__(self, a_star, width, height):

        pygame.init()
        self.solution = a_star.get_solution()
        self.a_star = a_star
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))

    def MainLoop(self):

        # Load All of our Sprites
        a_star.tiles.create_sprite_map()
        self.load_sprites()
        # tell pygame to keep sending up keystrokes when they are held down
        pygame.key.set_repeat(500, 30)

        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((145,145,145))

        solution_counter = -1
        finished = False
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == KEYDOWN:
                    if ((event.key == K_RIGHT)
                    or (event.key == K_LEFT)
                    or (event.key == K_UP)
                    or (event.key == K_DOWN)):
                        solution_counter = -1
                        tile = self.solution[-1]
                        finished = False
                        self.plane.rect.topleft = self.a_star.tiles.get_tile_sprite(tile.x, tile.y).rect.topleft
                        for p in a_star.planes:
                            p.energy = 5


            self.screen.blit(self.background, (0, 0))   
            a_star.tiles.tile_sprites_group.draw(self.screen)

            tile = self.solution[solution_counter]

            if pygame.font:
                for sprite, p in zip(self.pilots_sprites, self.pilots):
                    sprite.draw(self.screen)
                    font = pygame.font.Font(None, 22)
                    text_name = font.render("%s" %(p.plane.name), 1, (35, 35, 35))
                    text_codename = font.render("%s" %(p.plane.codename), 1, (35, 35, 35))
                    text_pilot = font.render("%s" %(p.plane.pilot), 1, (35, 35, 35))
                    text_power = font.render("Power: %.1f" %(p.plane.power), 1, (35, 35, 35))
                    text_energy = font.render("Energy: %d" %(p.plane.energy), 1, (35, 35, 35))
                    textpos = p.rect.topright
                    textpos_2 = (textpos[0] + 5,textpos[1] + 5)
                    textpos_3 = (textpos_2[0],textpos_2[1] + 20)
                    textpos_4 = (textpos_2[0],textpos_2[1] + 40)
                    textpos_5 = (textpos_2[0],textpos_2[1] + 60)
                    textpos_6 = (textpos_2[0],textpos_2[1] + 80)

                    self.screen.blit(text_name, textpos_2)
                    self.screen.blit(text_codename, textpos_3)
                    self.screen.blit(text_pilot, textpos_4)
                    self.screen.blit(text_power, textpos_5)
                    self.screen.blit(text_energy, textpos_6)

                text_cost = pygame.font.Font(None, 36).render("Cost: %.2f min" %(tile.g), 1, (35, 35, 35))
                textpos_cost = self.pilots[4].rect.bottomleft
                textpos_cost = (textpos_cost[0],textpos_cost[1] + 10)
                self.screen.blit(text_cost, textpos_cost)

            
            self.plane_sprite.draw(self.screen)
            pygame.display.flip()

            pygame.time.wait(100)

            
            if tile != self.a_star.end:
                solution_counter -= 1
                self.plane.rect.topleft = self.a_star.tiles.get_tile_sprite(tile.x, tile.y).rect.topleft


                if tile.planes_attackers is not None:
                    for plane in tile.planes_attackers:
                        plane.energy -= 1

                flying_planes = filter(lambda plane: plane.energy > 0, a_star.planes)
                if len(flying_planes) == 0:
                    print "\nTodos avioes foram ab\atidos! Tente de novo..."
                    break

            elif finished == False:
                self.plane.rect.topleft = self.a_star.tiles.get_tile_sprite(tile.x, tile.y).rect.topleft
                print '\n"Great shot kid! That was one in a million!" - Han Solo'
                finished = True


    def load_sprites(self):

        self.pilots_sprites = []
        self.pilots = []

        for i, plane in enumerate(self.a_star.planes):
            sprite = PilotSprite(i+2, self.a_star.planes[i])
            self.pilots.append(sprite)
            self.pilots_sprites.append(pygame.sprite.RenderPlain((sprite)))

        self.plane = PlaneSprite()
        self.plane_sprite = pygame.sprite.RenderPlain((self.plane))
        self.plane.rect.topleft = [0,0]        
        tile = self.solution[-1]
        self.plane.rect.topleft = self.a_star.tiles.get_tile_sprite(tile.x, tile.y).rect.topleft

if __name__ == "__main__":

    squad = [Plane("F-22 Raptor", 1.5, "Wedge Antilles", "Red 2"),
             Plane("F-35 Lighting", 1.4, "Biggs Darklighter", "Red 3"),
             Plane("T-50 PAK FA", 1.3, "John D. Branon", "Red 4"),
             Plane("Su-46", 1.2 , "Luke Skywalker", "Red 5"),
             Plane("MiG-35", 1.1, "Jek Porkins", "Red 6")]

    tilemap = Tilemap.get_tilemap("maze1.txt")
    tilemap.print_map_log()

    # hardcoded, pois a ordem das bases pedida no trabalho nao esta de acordo com a ordem em q elas aparecem
    enemy_bases = [(37,19),(31,17),(31,33),(24,26),(24,9),(17,9),(17,26),(13,36),(9,30),(9,14),(4,13)]
    base_cost = [60, 65, 70, 75, 80, 85, 90, 95, 100, 110, 120]
    a_star = AStar(tilemap, squad, enemy_bases, base_cost)

    print "Start: ", a_star.start.x, a_star.start.y
    print "End: ", a_star.end.x, a_star.end.y
    print "h w: ", tilemap.height, tilemap.width

    if a_star.start == None or a_star.end == None:
        print "Arquivo do mapa fora do padrao."
    else:
        print "Solving..."

        solution = a_star.find_path()

        if solution == None:
            print "Nao ha solucao"

        else:
            print "Caminho de tamanho: ", len(solution)
            
            for tile in solution:
                print "(%d, %d)   g: %.2f h: %.2f f: %.2f" %(tile.x, tile.y, tile.g, tile.h, tile.f)

            tilemap.print_solution_map(solution)

            
            total_cost = solution[0].g
            print "\nCusto total: %.2f" %(total_cost)
            print "\nAvioes sobreviventes:"
            for plane in a_star.planes:
                print plane

    MainWindow = Main(a_star, 1300, 1000)
    MainWindow.MainLoop()