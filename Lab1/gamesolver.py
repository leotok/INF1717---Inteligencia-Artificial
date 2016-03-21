# -*- coding: utf-8 -*-

### LIBRARIES:

from collections import deque

### SETUP:

ROOT = "C:\\Users\\e1312737.LAB-GRAD\\Documents\\ia161\\" 

file = open((ROOT + "maze41.txt"), "r+") # read table file

table = file.read() # tabuleiro

### PROCESS:

table = table.split('\n')


def pegaVizinhos(tupla, arq):
    
    run = list()
    
    takedown = list()
    
    run.append([tupla[0], tupla[1]+1])
    run.append([tupla[0], tupla[1]-1])
    run.append([tupla[0]+1, tupla[1]])
    run.append([tupla[0]-1, tupla[1]])
              
    for i in run: 
        if arq[i[0]][i[1]] == '.' and i[0] >= 0 and i[1] >= 0:
            takedown.append([i[0], i[1]])
               
    return(takedown)
    
def findEnd(arq):
    
    for i in range(1, len(arq)):
        for j in range(1, len(arq[i])):
            
            if arq[i][j] == 'F':
                
                return(i,j)
 

end = findEnd(table)
   
def findStart(arq):
    
    for i in range(1, len(arq)):
        for j in range(1, len(arq[i])):
            
            if arq[i][j] == 'I':
                
                return(i,j)
                
start = findStart(table)
   
def treeSearch(start):
    fila = deque()
    
    visited = list()
        
    fila.append(start) 
        
    while len(fila) > 0:
        valorAtual = fila.popleft()
        visited.append(valorAtual)
        
        if(table[valorAtual[0]][valorAtual[1]] != '.'):
            print(table[valorAtual[0]][valorAtual[1]])
        
        
        if (valorAtual == end):
            print('got it')
            return 1
            
        
    
        vizinhos = pegaVizinhos(valorAtual, table)
        
        for vizinho in vizinhos:
            
            try:
                visited.index(vizinho)
            
            except:
                fila.append(vizinho)

            
    