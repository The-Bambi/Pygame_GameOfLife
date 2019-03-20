import numpy as np
import matplotlib.pyplot as plt        
from IPython.display import clear_output
import matplotlib.pyplot as plt

class GoL:
    '''Game of Life class. Requires tuple or list with initial shape of the board.'''
    
    def __init__(self,shape):
        '''Board is larger by a row and column on each end to avoid index errors. Additional rows and column dont change'''
        self.gen = np.zeros((shape[0]+2,shape[1]+2))
        self.next = np.zeros((shape[0]+2,shape[1]+2))
    
    def show(self):
        plt.spy(self.gen[1:-1,1:-1])
        
    def add(self,coords):
        '''self.add(coords_list). Changes all coordinates from list to 1. Eg. self.add([[1,1],[1,2],[2,1],[2,2]]).'''
        for x in coords:
            self.gen[x[0],x[1]] = 1
    
    def _evolve(self):
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
        '''evolve(generations = 1, time_of_frame = 0.25)'''
        for gen in range(generations):
            self._evolve()
            plt.spy(self.gen[1:-1,1:-1])
            plt.pause(time_of_frame)
            clear_output(wait = "True")
        plt.show()
