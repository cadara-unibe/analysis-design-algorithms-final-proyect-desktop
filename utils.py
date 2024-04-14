from PyQt5.QtWidgets import QMessageBox

def is_float(text):
    try:
         value = int(text)
         return False
    except ValueError:
         return True
    
def show_error(error_message):
        error_box = QMessageBox()
        error_box.setWindowTitle("Error")
        error_box.setIcon(QMessageBox.Critical)
        error_box.setText(str(error_message))
        error_box.exec_()