
import numpy as np

class Matrix:
    def __init__(self, rows, cols):
        self.matrix = np.array(np.random.randint(1, 10, size=(rows, cols)))

    def to_numpy(self):
        return self.matrix

    def __str__(self):
        return str(self.matrix)