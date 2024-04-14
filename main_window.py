from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel
from matrix import Matrix

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

        central_widget.setLayout(layout)

        self.generate_button.clicked.connect(self.generate_matrices)

    def generate_matrices(self):
        rows = int(self.rows_input.text())
        cols = int(self.cols_input.text())
        self.matrix_a = Matrix(rows, cols)
        self.matrix_b = Matrix(rows, cols)
        self.result_label.setText(str(self.matrix_a) + "\n\n" + str(self.matrix_b))

