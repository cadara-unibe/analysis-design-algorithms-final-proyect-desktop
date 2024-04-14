import numpy as np

class MatrixOperations:
    @staticmethod
    def add(matrix_a, matrix_b):
        return matrix_a + matrix_b

    @staticmethod
    def subtract(matrix_a, matrix_b):
        return matrix_a - matrix_b

    @staticmethod
    def multiply(matrix_a, matrix_b):
        return np.dot(matrix_a, matrix_b)

    @staticmethod
    def divide(matrix_a, matrix_b):
        return np.divide(matrix_a, matrix_b)
