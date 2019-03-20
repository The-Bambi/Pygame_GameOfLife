import numpy as np
from time import time
from pygame import draw

class GoL:
    '''Game of Life class. Requires tuple or list with initial shape of the board.'''
    
    def __init__(self, shape, screen):
        '''Board is larger by a row and column on each end to avoid index errors. Additional rows and column dont change'''
        self.gen = np.zeros((shape[0]+2,shape[1]+2))
        self.next = np.zeros((shape[0]+2,shape[1]+2))
        self.lastUpdate = time()
        self.updateFreq = 0.5
        self.screen = screen

    def add(self,coords):
        '''self.add(coords_list). Changes all coordinates from list to 1. Eg. self.add([[1,1],[1,2],[2,1],[2,2]]).'''
        for x in coords:
            self.gen[x[0],x[1]] = 1
    
    def _evolve(self):
        if time() - self.lastUpdate > self.updateFreq:
            '''Hidden function that evolves current generation to the next one.'''
            for b,c in enumerate(self.gen[1:-1],1):
                for d,e in enumerate(c[1:-1],1):
                    window = self.gen[b-1:b+2, d-1:d+2]
                    cell = int(window[1,1])
                    count = np.count_nonzero(np.delete(window,4))
                    if cell == 1 and count<2:
                        self.next[b,d] = 0
                    if cell == 1 and count<4 and count>1:
                        self.next[b,d] = 1
                    if cell == 1 and count>3:
                        self.next[b,d] = 0
                    if cell == 0 and count == 3:
                        self.next[b,d] = 1
            self.gen = self.next.copy()

    def evolve(self,generations = 1, time_of_frame = 0.25):
        for gen in range(generations):
            self._evolve()

    def show(self):
        for y_index, line in enumerate(self.gen.T):
            for x_index, pixl in enumerate(line):
                if pixl == 0:
                    color = (0,0,0)
                if pixl == 1:
                    color = (255,255,255)
                draw.rect(self.screen, (255,255,255, 20), (x_index*9, y_index*9, 9, 9),1)
                draw.rect(self.screen, color, (x_index*9+1, y_index*9+1, 7, 7))