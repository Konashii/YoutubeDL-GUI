# Tutorial used: https://www.pythontutorial.net/pyqt/

import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QGridLayout, QLineEdit, QCheckBox, QWidget, QVBoxLayout, QPushButton, QFileDialog
)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
from src import youtubedl

class MainWindow(QWidget):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # VARIABLES
        self.vid_total_length = 0
        self.vid_total_space = 0
        self.title_list = []
        self.url_list = []
        self.directory = ""
        
        self.setWindowTitle('Youtube Downloader GUI')
        self.setGeometry(100, 100, 500, 300)
        
        # WIDGETS
        self.url_edit = QLineEdit(placeholderText="URL of Video...")
        self.url_add_btn = QPushButton("+")
        self.left_side = QWidget(self)
        self.right_side = QWidget(self)
        self.properties = QWidget(self.left_side)
        self.title_list_widget = QWidget(self.right_side)
        self.destination_btn = QPushButton("Destination")
        self.download_btn = QPushButton("Download")
        self.information_label = QWidget(self.right_side)
        self.total_length_label = QLabel("Total Length: 0")
        self.total_space_label = QLabel("Total Space: 0")
        self.audio_only = QCheckBox("Audio only", self.properties)
        
        self.layout = QGridLayout()
        self.left_layout = QGridLayout()
        self.right_layout = QGridLayout()
        self.properties_layout = QGridLayout()
        self.title_list_layout = QVBoxLayout()
        self.information_layout = QGridLayout()
        
        # Button function connectivity
        self.url_add_btn.clicked.connect(lambda: self.get_video_info())
        self.destination_btn.clicked.connect(lambda: self.set_destination())
        self.download_btn.clicked.connect(lambda: self.download_videos())
        
        # STYLING
        self.setStyleSheet("background-color: #222222;")
        self.properties.setStyleSheet("background-color: #5A5A5A; font-size: 10px;")
        self.title_list_widget.setStyleSheet("background-color: #5A5A5A;")
        self.information_label.setStyleSheet("background-color: #5A5A5A;")
        
        self.setLayout(self.layout)
        self.left_side.setLayout(self.left_layout)
        self.right_side.setLayout(self.right_layout)
        self.properties.setLayout(self.properties_layout)
        self.title_list_widget.setLayout(self.title_list_layout)
        self.information_label.setLayout(self.information_layout)
                
        # ADDING WIDGETS
        self.layout.addWidget(self.left_side, 0, 0)
        self.layout.addWidget(self.right_side, 0, 1)
        
        self.right_layout.addWidget(self.url_edit, 0, 0)
        self.right_layout.addWidget(self.title_list_widget, 1, 0, 1, 0)
        self.right_layout.addWidget(self.url_add_btn, 0, 1)
        self.right_layout.addWidget(self.information_label, 2, 0, 1, 0)
        self.left_layout.addWidget(self.properties)
        self.left_layout.addWidget(self.destination_btn)
        self.left_layout.addWidget(self.download_btn)
        self.information_layout.addWidget(self.total_length_label)
        self.information_layout.addWidget(self.total_space_label)
        
        self.show()


    def on_checked_box(self):
        state = Qt.CheckState(self.audio_only)
        
        if state == Qt.CheckState.Checked:
            self.audio_only_bool = True
        else:
            self.audio_only_bool = False

    # Clears out title list for a fresh restart
    def clear_titles(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

    # This is a function for a universal update (updates everything)
    def refresh_ui(self) -> None:
        self.total_length_label.setText(f"Total Length: {round(self.vid_total_length, 2)} Minute(s)")
        self.total_space_label.setText(f"Total Space: {round(self.vid_total_space, 1)} MB")

        self.clear_titles(self.title_list_layout)
        
        for title in self.title_list:
            label = QLabel(title)
            self.title_list_layout.addWidget(label)

    # Uses video_info function to extract data and put it on the Widgets
    def get_video_info(self) -> None:
        try:
            url = self.url_edit.text()
            data = youtubedl.video_info(url)

            self.vid_total_length += data["duration"]/60 # Converts from seconds to minutes
            self.vid_total_space += data["filesize"]/1000000 # Converts from bytes to Megabytes
            
            # Adds title to the title list to create widgets
            self.title_list.append(data["title"])
            self.url_list.append(url)
            
        except Exception as e:
            # This is so that there's no error which results in app closing.
            #print(f"Couldn't get video info: {e}")
            return
        
        self.url_edit.setText("")
        self.refresh_ui()
        
        
    def set_destination(self) -> None:
        self.directory = QFileDialog.getExistingDirectory(self, "Select Folder", "./")
        
    
    def download_videos(self) -> None:
        audio_only = self.audio_only.isChecked()
        
        for url in self.url_list:
            youtubedl.download_video(url, self.directory, audio_only)
            
        # Resetting values for a fresh start
        self.title_list.clear()
        self.url_list.clear()
        self.vid_total_length = 0
        self.vid_total_space = 0
        self.refresh_ui()
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    window = MainWindow()
    sys.exit(app.exec())