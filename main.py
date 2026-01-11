import sys
from PyQt6.QtWidgets import QApplication
from src import MainWindow

# TODO: Make a script that takes a directory/file as input and count lines of code.

def main():
    app = QApplication(sys.argv)
    
    window = MainWindow()
    sys.exit(app.exec())
    
if __name__ == '__main__':
    main()