import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout


def ggui():
    app = QApplication([])
    window = QWidget()
    layout = QVBoxLayout()
    
    layout.addWidget(QPushButton('Top'))
    layout.addWidget(QPushButton('Bottom'))
    window.resize(500,500)
    window.setLayout(layout)
    window.show()
    app.exec_() 

if __name__ == "__main__":
        ggui()