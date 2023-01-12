import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class QPushButtonIcon(QPushButton):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setFixedHeight(200)
        self.setFixedWidth(200)
        self.setIconSize(QSize(192, 192))

class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.set_default()
        self.set_style()
        self.init_ui()

    def set_default(self):
        self.selection_list = []

        self.figures = ['./파충류_양서류/이름X/카멜레온.png']

        self.icons = {}

        for index, filename in enumerate(self.figures):
            pixmap = QPixmap(filename)
            pixmap = pixmap.scaled(200,200,Qt.IgnoreAspectRatio)
            icon = QIcon()
            icon.addPixmap(pixmap)
            self.icons[index] = icon

    def set_style(self):
        with open("style", 'r') as f:
            self.setStyleSheet(f.read())

    def init_ui(self):
        main_layout = QVBoxLayout()

        self.qbuttons = {}
        for index, icon in self.icons.items():
            button = QPushButtonIcon()
            button.setIcon(icon)
            button.clicked.connect(lambda state, button = button, idx = index :
                                   self.qbutton_clicked(state, idx, button))
            main_layout.addWidget(button)
            self.qbuttons[index] = button

        main_layout.addLayout(main_layout)

        self.setLayout(main_layout)
        self.setFixedSize(main_layout.sizeHint())
        self.setWindowTitle("FlashCard Game")
        self.show()

        # 이미지 버튼을 눌렀을 경우 이벤트
    def qbutton_clicked(self, state, idx, button):
        self.selection_list.append(idx)
        self.changeFigures = ['./파충류_양서류/이름O/카멜레온.png']

        pixmap = QPixmap('./파충류_양서류/이름O/카멜레온.png')
        pixmap = pixmap.scaled(200, 200, Qt.IgnoreAspectRatio)

        icon = QIcon()
        icon.addPixmap(pixmap)

        button.setIcon(icon)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())