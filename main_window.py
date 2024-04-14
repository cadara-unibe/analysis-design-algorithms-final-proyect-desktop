from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel
from matrix import Matrix
from matrix_calculator import MatrixOperations

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Operaciones con Matrices")
        self.setGeometry(100, 100, 400, 300)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        self.rows_label = QLabel("Cantidad de Filas")
        layout.addWidget(self.rows_label)
        self.rows_input = QLineEdit()
        layout.addWidget(self.rows_input)
        
        self.columns_label = QLabel("Cantidad de Columnas")
        layout.addWidget(self.columns_label)
        self.cols_input = QLineEdit()
        layout.addWidget(self.cols_input)

        self.generate_button = QPushButton("Generar Matrices")
        layout.addWidget(self.generate_button)

        self.result_label = QLabel()
        layout.addWidget(self.result_label)

        self.addition_button = QPushButton("Sumar Matrices")
        layout.addWidget(self.addition_button)

        self.substraction_button = QPushButton("Restar Matrices")
        layout.addWidget(self.substraction_button)

        self.multiplication_button = QPushButton("Multiplicar Matrices")
        layout.addWidget(self.multiplication_button)

        self.division_button = QPushButton("Dividir Matrices")
        layout.addWidget(self.division_button)

        self.operations_result_label_title = QLabel("Resultado:")
        layout.addWidget(self.operations_result_label_title)
        self.operations_result_label = QLabel()
        layout.addWidget(self.operations_result_label)

        central_widget.setLayout(layout)

        self.generate_button.clicked.connect(self.generate_matrices)

        self.addition_button.clicked.connect(self.action_add_matrix)
        self.substraction_button.clicked.connect(self.action_substract_matrix)
        self.multiplication_button.clicked.connect(self.action_multiply_matrix)
        self.division_button.clicked.connect(self.action_divide_matrix)

    def generate_matrices(self):
        rows = int(self.rows_input.text())
        cols = int(self.cols_input.text())
        self.matrix_a = Matrix(rows, cols)
        self.matrix_b = Matrix(rows, cols)
        self.result_label.setText(str(self.matrix_a) + "\n\n" + str(self.matrix_b))

    def action_add_matrix(self):
        self.matrix_result = MatrixOperations.add(self.matrix_a, self.matrix_b)
        self.operations_result_label.setText(str(self.matri))

    def action_substract_matrix(self):
        self.matrix_result = MatrixOperations.subtract(self.matrix_a, self.matrix_b)
        self.operations_result_label.setText(str(self.matri))

    def action_multiply_matrix(self):
        self.matrix_result = MatrixOperations.multiply(self.matrix_a, self.matrix_b)
        self.operations_result_label.setText(str(self.matri))

    def action_divide_matrix(self):
        self.matrix_result = MatrixOperations.divide(self.matrix_a, self.matrix_b)
        self.operations_result_label.setText(str(self.matri))

