import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget, QLabel


# Наше приложение - сюда добавляется 1 главный виджет
class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 tabs'
        self.left = 0
        self.top = 0
        self.width = 300
        self.height = 200
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)
        self.show()


class FirstTab(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.initUi()

    def initUi(self):
        self.label = QLabel(self)
        self.label.setText("Первый таб")
        self.button = QPushButton(self)
        self.button.move(0, 40)
        self.button.setText("Нажми меня")
        self.button.clicked.connect(self.clickHandler)

    def clickHandler(self):
        self.parent.infoFromTab("Щелкнули в первом")


class SecondTab(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.initUi()

    def initUi(self):
        self.label = QLabel(self)
        self.label.setText("Второй таб")
        self.button = QPushButton(self)
        self.button.move(0, 40)
        self.button.setText("Нажми меня")
        self.button.clicked.connect(self.clickHandler)

    def clickHandler(self):
        self.parent.infoFromTab("Щелкнули во втором")


# Главный виджет содержит в себе label для вывода информации и переключатель табов
# Табы могут взаимодействовать со своим родителем, если прокинуть им ссылку на родительский класс, как в этом примере
class MyTableWidget(QWidget):

    def __init__(self, parent):
        super().__init__(parent)

        # Initialize tab screen
        self.label = QLabel(self)
        self.label.setText("Нет событий")

        self.tabs = QTabWidget(self)
        self.tab1 = FirstTab(self)
        self.tab2 = SecondTab(self)
        self.tabs.resize(300, 200)
        self.tabs.move(0, 20)

        # Add tabs
        self.tabs.addTab(self.tab1, "Tab 1")
        self.tabs.addTab(self.tab2, "Tab 2")

    def infoFromTab(self, info):
        self.label.setText(info)
        self.label.adjustSize()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
