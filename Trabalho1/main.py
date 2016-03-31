# LIBRARIES:

from collections import deque
from tree import Tree
from plane import Plane

# Funcao para pegar os vizinhos de um no da matriz que nao estao bloqueados com 'X'

def pegaVizinhos(tupla, mat):
    run = [(tupla[0], tupla[1] + 1), (tupla[0], tupla[1] - 1), (tupla[0] + 1, tupla[1]), (tupla[0] - 1, tupla[1])]
    vizinhos = list()

    for i in run:

        try:

            if (mat[i[0]][i[1]] != 'M') and i[0] >= 0 and i[1] >= 0:
                vizinhos.append((i[0], i[1]))

        except IndexError:

            print("end of matrix file reached")

    return vizinhos


# Funcao para achar a posicao final no Maze representado por 'F'

def findEnd(mat):
    for i in range(1, len(mat)):
        for j in range(1, len(mat[i])):

            if mat[i][j] == 'F':
                return (i, j)

# Funcao para achar a posicao inicial no Maze representado por 'I'

def findStart(mat):
    for i in range(0, len(mat)):
        for j in range(0, len(mat[i])):

            if mat[i][j] == 'I':
                return (i, j)

# Funcao para executar a busca em largura e achar o caminho de 'I' a 'F'

def bfs_search(start, end):

    visited = list()
    fila = deque()
    fila.append(start)

    t_root = Tree(start)

    while len(fila) > 0:

        valorAtual = fila.popleft()

        if valorAtual not in visited:
            visited.append(valorAtual)

        t = t_root.get_node_of_value(valorAtual)

        if valorAtual == end:
            print('got it')
            return t.get_trail_from_node()

        matrix_run[valorAtual[0]][valorAtual[1]] = 'o'

        vizinhos = pegaVizinhos(valorAtual, matrix)

        for vizinho in vizinhos:

            if vizinho not in visited and vizinho not in fila:
                fila.append(vizinho)
                t.add_child(Tree(vizinho))

    return None

# main:

squad = [Plane("F-22 Raptor", 1.5),
         Plane("F-35 Lighting", 1.4),
         Plane("T-50 PAK FA", 1.3),
         Plane("Su-46", 1.2),
         Plane("MiG-35", 1.1)]


arq = open(("maze1.txt"), "r+")
matrix = arq.read()
arq.close()

# PROCESS:

matrix = matrix.split('\n')


# copia matrix pra matrix_percorrida que ira imprimir a matriz com o caminho
matrix_run = map(list, matrix)
matrix_solution = map(list, matrix)

start = findStart(matrix)
print "Start: " + str(start)
end = findEnd(matrix)
print 'End: ' + str(end)

# final bfs_search
if start == None or end == None:
    print "Arquivo do mapa fora do padrao."
else:
    solution = bfs_search(start, end)

    if solution == None:
        print "Nao ha solucao"

    else:
        print "Caminho de tamanho: " + str(len(solution))
        print solution

        for i in solution:
            matrix_solution[i.value[0]][i.value[1]] = '>'

        print "Caminho solucao: \n"
        for line in matrix_solution:
            print line

    print "Todos caminhos percorridos: \n"
    for line in matrix_run:
        print line