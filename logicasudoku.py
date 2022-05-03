import numpy as np
class Cuerpo():
    def __init__(self):
        self.cuerpo = np.array([[]])

    def iniciarcuerpo(self):
        self.cuerpo = np.array([[0,0,0,0,0,0,0,0,0],
                                [0,0,0,0,0,0,0,0,0],
                                [0,0,0,0,0,0,0,0,0],
                                [0,0,0,0,0,0,0,0,0],
                                [0,0,0,0,0,0,0,0,0],
                                [0,0,0,0,0,0,0,0,0],
                                [0,0,0,0,0,0,0,0,0],
                                [0,0,0,0,0,0,0,0,0],
                                [0,0,0,0,0,0,0,0,0]])

    def imprimirtabla(self):
        print(self.cuerpo)

