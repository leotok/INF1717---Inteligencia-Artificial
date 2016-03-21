### LIBRARIES:

from collections import deque

### SETUP:

ROOT = "C:\\Users\\e1312737.LAB-GRAD\\Documents\\ia161\\"
ROOT_Leo = "/Users/LeoWajnsztok/Documents/Python/INF1771/Lab1/"

file = open(( "maze41.txt"), "r+")

table = file.read()

### PROCESS:

table = table.split('\n')
# copia table pra table_percorrida que ira imprimir a matriz com o caminho
table_percorrida = map(list,table)


# Funcao para pegar os vizinhos de um no da matriz que nao estao bloqueados com 'X'

def pegaVizinhos(tupla, arq):

    run = list()

    vizinhos = list()

    run.append([tupla[0], tupla[1]+1])
    run.append([tupla[0], tupla[1]-1])
    run.append([tupla[0]+1, tupla[1]])
    run.append([tupla[0]-1, tupla[1]])

    for i in run:
        if ( arq[i[0]][i[1]] == '.' or arq[i[0]][i[1]] == 'F') and i[0] >= 0 and i[1] >= 0:
            vizinhos.append([i[0], i[1]])

    return(vizinhos)

# Funcao para achar a posicao final no Maze representado por 'F'

def findEnd(arq):

    for i in range(1, len(arq)):
        for j in range(1, len(arq[i])):

            if arq[i][j] == 'F':

                return[i,j]


end = findEnd(table)
print 'End: ' + str(end)

# Funcao para achar a posicao inicial no Maze representado por 'I'

def findStart(arq):

    for i in range(1, len(arq)):
        for j in range(1, len(arq[i])):

            if arq[i][j] == 'I':

                return(i,j)

start = findStart(table)

# Funcao para executar a busca em largura e achar o caminho de 'I' a 'F'

def treeSearch(start):
    fila = deque()

    visited = list()

    fila.append(start)

    while len(fila) > 0:
        valorAtual = fila.popleft()
        visited.append(valorAtual)

        if valorAtual == end:
            print('got it')
            return 1

        table_percorrida[valorAtual[0]][valorAtual[1]] = 'o'

        vizinhos = pegaVizinhos(valorAtual, table)

        for vizinho in vizinhos:

            try:
                visited.index(vizinho)

            except:
                fila.append(vizinho)
    return 0

print treeSearch(start)

for line in table_percorrida:
    print line