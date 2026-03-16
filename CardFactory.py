from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6 import *
from PyQt6.QtCore import Qt
class CardFactory:
    def create_card():
        card = QFrame()
        
        layout = QVBoxLayout(card)
        
        img_label = QLabel()
        pixmap = QPixmap(r'img\tarot\01_TheFool.png')
        img_label.setPixmap(pixmap.scaled(150, 200, Qt.AspectRatioMode.KeepAspectRatio))
        
        layout.addWidget(img_label)
        return card
    