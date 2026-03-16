import sys
import tarotcard
from PyQt6.QtWidgets import *
class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.setWindowTitle('The Fools Journey')
        self.setGeometry(0,0, 908, 680)
        
        card = tarotcard.CardFactory.create_card()
        

        layout = QHBoxLayout()
        layout.addWidget(card)
        layout.addWidget(tarotcard.CardFactory.create_card())
        self.setLayout(layout)

        self.show()
        
    def button_clicked(self):
        print('clicked')
        
    
        
def loadStyleSheet(app, filename):
        with open(filename, "r") as f:
            style = f.read()
            app.setStyleSheet(style)
              
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    loadStyleSheet(app, "style.qss")
    sys.exit(app.exec())
    
