import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QMainWindow, QLabel


class FirstForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Главная форма')

        self.btn = QPushButton('Другая форма', self)
        self.btn.resize(100, 100)
        self.btn.move(100, 100)

        self.btn.clicked.connect(self.open_second_form)

    def open_second_form(self):
        self.second_form = SecondForm(self, "Данные для второй формы")
        self.second_form.setGeometry(200, 200, 200, 200)
        self.second_form.show()


class SecondForm(QWidget):
    def __init__(self, parent, data):
        super().__init__()
        self.parent = parent  # с помощью ссылки на родителя мы можем вызывать его методы для взаимодействия
        self.initUI(data)

    def initUI(self, data):
        self.setWindowTitle('Вторая форма')
        self.lbl = QLabel(data, self)
        self.lbl.adjustSize()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FirstForm()
    ex.show()
    sys.exit(app.exec())
