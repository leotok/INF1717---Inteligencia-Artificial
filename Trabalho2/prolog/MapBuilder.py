
class MapBuilder:

    def __init__(self, prolog_bridge, arq):

        self.map_file = open(arq, 'r')

        self.map_file = self.map_file.read()

        self.map_file = self.map_file.split('\n')

        for i in range(0, len(self.map_file)):
            for j in range(0, len(self.map_file[i])):

                if(self.map_file[i][j] == 'P'):

                    prolog_bridge.prolog.assertz('tile('+str(i+1)+','+str(j+1)+',[pit]).')

                elif(self.map_file[i][j] == 'O'):

                    prolog_bridge.prolog.assertz('tile('+str(i+1)+','+str(j+1)+',[ouro]).')

                elif(self.map_file[i][j] == 'T'):

                     prolog_bridge.prolog.assertz('tile('+str(i+1)+','+str(j+1)+',[transporte]).')

                
