import os, sys
import pygame
from helpers import *
from pygame.locals import *
from collections import deque

from plane import *
from tile import *
from AStar import *

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

def get_tilemap(arq):

    with open(arq, "r") as f:
        matrix = f.read()

    matrix = matrix.split('\n') 
    tilemap = Tilemap(matrix)
    return tilemap

# Main:

if __name__ == "__main__":

    squad = [Plane("F-22 Raptor", 1.5),
             Plane("F-35 Lighting", 1.4),
             Plane("T-50 PAK FA", 1.3),
             Plane("Su-46", 1.2),
             Plane("MiG-35", 1.1)]

    tilemap = get_tilemap("maze1.txt")
    tilemap.print_map_log()

    enemy_bases = [(37,19),(31,17),(31,33),(24,26),(24,9),(17,9),(17,26),(13,36),(9,30),(9,14),(4,13)]
    a_star = AStar(tilemap, squad, enemy_bases)

    print "Start: ", a_star.start.x, a_star.start.y
    print "End: ", a_star.end.x, a_star.end.y
    print "h w: ", tilemap.height, tilemap.width

    if a_star.start == None or a_star.end == None:
        print "Arquivo do mapa fora do padrao."
    else:
        print "Solving:\n"

        solution = a_star.find_path()

        if solution == None:
            print "Nao ha solucao"

        else:
            print "Caminho de tamanho: ", len(solution)
            print solution

            tilemap.print_solution_map(solution)
            
            print "Avioes sobreviventes:"
            for plane in a_star.planes:
                print plane