from PyQt5.QtWidgets import QMessageBox

def is_float(text):
    try:
        float(text)
        return True
    except ValueError:
        return False
    
def show_error(self, error_message):
        error_box = QMessageBox()
        error_box.setWindowTitle("Error")
        error_box.setIcon(QMessageBox.Critical)
        error_box.setText(str(error_message))
        error_box.exec_()