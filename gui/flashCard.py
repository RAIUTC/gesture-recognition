import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class QPushButtonIcon(QPushButton):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setFixedHeight(700)
        self.setFixedWidth(700)
        self.setIconSize(QSize(692, 692))

class Main(QDialog):
    QPushButtonCount = 0

    def __init__(self):
        super().__init__()
        self.set_default()
        self.set_style()
        self.init_ui()

    def set_default(self):
        pixmap = QPixmap('./파충류_양서류/이름X/카멜레온.png')
        pixmap = pixmap.scaled(700, 700, Qt.IgnoreAspectRatio)
        self.icon = QIcon()
        self.icon.addPixmap(pixmap)

    def set_style(self):
        with open("style", 'r') as f:
            self.setStyleSheet(f.read())

    def init_ui(self):
        main_layout = QVBoxLayout()

        button = QPushButtonIcon()
        button.setIcon(self.icon)

        button.clicked.connect(lambda state, button = button:
                               self.qbutton_clicked(button))
        main_layout.addWidget(button)

        self.setLayout(main_layout)
        self.setFixedSize(main_layout.sizeHint())
        self.setWindowTitle("FlashCard Game")
        self.show()

        # 이미지 버튼을 눌렀을 경우 이벤트
    def qbutton_clicked(self, button):
        self.QPushButtonCount = self.QPushButtonCount + 1
        print(self.QPushButtonCount)

        self.chageIcons = [
            './파충류_양서류/이름X/카멜레온.png', './파충류_양서류/이름O/카멜레온.png',
        './파충류_양서류/이름X/이구아나.png', './파충류_양서류/이름O/이구아나.png',
        './파충류_양서류/이름X/코모도왕도마뱀.png', './파충류_양서류/이름O/코모도왕도마뱀.png',
        './파충류_양서류/이름X/영원.png', './파충류_양서류/이름O/영원.png',
        './파충류_양서류/이름X/도롱뇽.png', './파충류_양서류/이름O/도롱뇽.png',
        './파충류_양서류/이름X/집도마뱀붙이.png', './파충류_양서류/이름O/집도마뱀붙이.png',
        './파충류_양서류/이름X/청개구리.png', './파충류_양서류/이름O/청개구리.png',
        './파충류_양서류/이름X/바다 거북.png', './파충류_양서류/이름O/바다 거북.png',
        './파충류_양서류/이름X/알다브라육지거북.png', './파충류_양서류/이름O/알다브라육지거북.png',
        './파충류_양서류/이름X/아나콘다.png', './파충류_양서류/이름O/아나콘다.png',
        './파충류_양서류/이름X/아흘로틀.png', './파충류_양서류/이름O/아흘로틀.png',
        './파충류_양서류/이름X/가리알.png', './파충류_양서류/이름O/가리알.png',
        './파충류_양서류/이름X/바다악어.png', './파충류_양서류/이름O/바다악어.png',
        './파충류_양서류/이름X/곡경아목.png', './파충류_양서류/이름O/곡경아목.png',
        ]

        pixmap = QPixmap(self.chageIcons[self.QPushButtonCount])
        pixmap = pixmap.scaled(700, 700, Qt.IgnoreAspectRatio)
        icon = QIcon()
        icon.addPixmap(pixmap)
        button.setIcon(icon)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
