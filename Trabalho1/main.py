# LIBRARIES:

import os, sys
import pygame
from helpers import *
from pygame.locals import *
from collections import deque

from tree import Tree
from plane import Plane
from tile import *
from AStart import *


if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'
# Funcao para pegar os vizinhos de um no da matriz que nao estao bloqueados com 'X'

def get_tilemap(arq):

    with open(arq, "r") as f:
        matrix = f.read()

    matrix = matrix.split('\n') 
    tilemap = Tilemap(matrix)
    return tilemap

# Funcao para executar a busca em largura e achar o caminho de 'I' a 'F'

# def find_path(start, end, tilemap):

#     visited = list()
#     fila = deque()
#     fila.append(start)

#     t_root = Tree(start)

#     while len(fila) > 0:

#         valorAtual = fila.popleft()

#         if valorAtual not in visited:
#             visited.append(valorAtual)

#         t = t_root.get_node_of_value(valorAtual)

#         if valorAtual == end:
#             print('got it')
#             return t.get_trail_from_node()

#         vizinhos = getNeighbours(valorAtual, tilemap)

#         for vizinho in vizinhos:

#             if vizinho not in visited and vizinho not in fila:
#                 fila.append(vizinho)
#                 t.add_child(Tree(vizinho))

#     return None


# Main:

if __name__ == "__main__":

    squad = [Plane("F-22 Raptor", 1.5),
             Plane("F-35 Lighting", 1.4),
             Plane("T-50 PAK FA", 1.3),
             Plane("Su-46", 1.2),
             Plane("MiG-35", 1.1)]

    tilemap = get_tilemap("maze1.txt")
    tilemap.print_map_log()

    a_star = AStar(tilemap)

    print "Start: ", a_star.start.x, a_star.start.y
    print "End: ", a_star.end.x, a_star.end.y
    print "h w: ", tilemap.height, tilemap.width



    if a_star.start == None or a_star.end == None:
        print "Arquivo do mapa fora do padrao."
    else:
        print "Solving:\n"

        solution = a_star.find_path(squad)

        if solution == None:
            print "Nao ha solucao"

        else:
            print "Caminho de tamanho: ", len(solution)
            print solution

            tilemap.print_solution_map(solution)
            