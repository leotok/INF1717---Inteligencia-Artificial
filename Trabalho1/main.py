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
        self.background.fill((0,0,0))

        solution_counter = -1
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
                        self.plane.rect.topleft = self.a_star.tiles.get_tile_sprite(tile.x, tile.y).rect.topleft


            self.screen.blit(self.background, (0, 0))   
            a_star.tiles.tile_sprites_group.draw(self.screen)
            self.plane_sprites.draw(self.screen)
            pygame.display.flip()

            pygame.time.wait(100)

            tile = self.solution[solution_counter]
            if tile != self.a_star.end:
                solution_counter -= 1
                self.plane.rect.topleft = self.a_star.tiles.get_tile_sprite(tile.x, tile.y).rect.topleft
            else:
                self.play_death_star_destruction_video()          


    def load_sprites(self):

        self.plane = PlaneSprite()
        self.plane_sprites = pygame.sprite.RenderPlain((self.plane))
        self.plane.rect.topleft = [0,0]        
        tile = self.solution[-1]
        self.plane.rect.topleft = self.a_star.tiles.get_tile_sprite(tile.x, tile.y).rect.topleft
            

    def play_death_star_destruction_video(self):

        movie = pygame.movie.Movie("death_start_destruction.mp4")
        self.screen = pygame.display.set_mode(movie.get_size())
        movie_screen = pygame.Surface(movie.get_size()).convert()
        movie.set_display(movie_screen)
        movie.play()

        self.blit(movie_screen, (0,0))
        pygame.display.update()


if __name__ == "__main__":

    squad = [Plane("F-22 Raptor", 1.5),
             Plane("F-35 Lighting", 1.4),
             Plane("T-50 PAK FA", 1.3),
             Plane("Su-46", 1.2),
             Plane("MiG-35", 1.1)]

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

            for tile in solution:
                if tile.planes_attackers is not None:
                    print tile.x, tile.y, tile.planes_attackers
                    for plane in tile.planes_attackers:
                        plane.energy -= 1

            flying_planes = filter(lambda plane: plane.energy > 0, a_star.planes)

            if len(flying_planes) == 0:
                print "\nTodos avioes foram ab\atidos! Tente de novo..."
            else:
                total_cost = solution[0].g
                print "\nCusto total: %.2f" %(total_cost)
                print "\nAvioes sobreviventes:"
                for plane in a_star.planes:
                    print plane

    MainWindow = Main(a_star, 1000, 1000)
    MainWindow.MainLoop()