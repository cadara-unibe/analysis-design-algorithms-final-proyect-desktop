import numpy as np

class MatrixOperations:
    @staticmethod
    def add(matrix_a, matrix_b):
        return np.add(matrix_a.to_numpy(), matrix_b.to_numpy())

    @staticmethod
    def subtract(matrix_a, matrix_b):
        return np.subtract(matrix_a.to_numpy(), matrix_b.to_numpy())

    @staticmethod
    def multiply(matrix_a, matrix_b):
        return np.dot(matrix_a.to_numpy(), matrix_b.to_numpy())

    @staticmethod
    def divide(matrix_a, matrix_b):
        return np.divide(matrix_a.to_numpy(), matrix_b.to_numpy())
