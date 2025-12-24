# Tutorial used: https://www.pythontutorial.net/pyqt/

import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QGridLayout, QLineEdit, QCheckBox, QWidget, QVBoxLayout, QPushButton
)
from PyQt6.QtGui import QFont


class MainWindow(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.setWindowTitle('Youtube Downloader GUI')
        self.setGeometry(100, 100, 320, 210)
        
        # WIDGETS
        url_edit = QLineEdit(placeholderText="URL of Video...")
        url_add_btn = QPushButton("+")
        left_side = QWidget(self)
        right_side = QWidget(self)
        properties = QWidget(left_side)
        url_list = QWidget(right_side)
        destination_btn = QPushButton("Destination")
        download_btn = QPushButton("Download")
        information_label = QWidget(right_side)
        total_length = QLabel("Total Length: ")
        total_space = QLabel("Total Space: ")
        
        layout = QGridLayout()
        left_layout = QGridLayout()
        right_layout = QGridLayout()
        properties_layout = QGridLayout()
        url_list_layout = QGridLayout()
        information_layout = QGridLayout()
        
        # STYLING
        self.setStyleSheet("background-color: #222222;")
        properties.setStyleSheet("background-color: #5A5A5A;")
        url_list.setStyleSheet("background-color: #5A5A5A;")
        information_label.setStyleSheet("background-color: #5A5A5A;")
        
        self.setLayout(layout)
        left_side.setLayout(left_layout)
        right_side.setLayout(right_layout)
        properties.setLayout(properties_layout)
        url_list.setLayout(url_list_layout)
        information_label.setLayout(information_layout)
                
        # ADDING WIDGETS
        layout.addWidget(left_side, 0, 0)
        layout.addWidget(right_side, 0, 1)
        
        right_layout.addWidget(url_edit, 0, 0)
        right_layout.addWidget(url_list, 1, 0, 1, 0)
        right_layout.addWidget(url_add_btn, 0, 1)
        right_layout.addWidget(information_label, 2, 0, 1, 0)
        left_layout.addWidget(properties)
        left_layout.addWidget(destination_btn)
        left_layout.addWidget(download_btn)
        information_layout.addWidget(total_length)
        information_layout.addWidget(total_space)
        
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    window = MainWindow()
    sys.exit(app.exec())