import numpy as np

class Matrix:
    def __init__(self, rows, cols):
        self.matrix = np.random.randint(1, 10, size=(rows, cols))

    def __str__(self):
        return str(self.matrix)
