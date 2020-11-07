import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit
import copy


# Пример со связанным редактированием данных об учениках
# FirstForm - основная форма приложения
# SecondForm - форма редактирования данных

class FirstForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Главная форма')
        # Задаем подписи к данным
        self.lbl1 = QLabel(self)
        self.lbl1.setText("Имя:")
        self.lbl1.move(0, 0)
        self.lbl1.adjustSize()
        self.lbl2 = QLabel(self)
        self.lbl2.setText("Рейтинг:")
        self.lbl2.move(0, 40)
        self.lbl1.adjustSize()

        # Одна запись в моих данных, представленная словарем data
        self.data = {"name": "Иван", "rating": 100}

        # Создадим label'ы для отображения данных, расположим их на форме
        self.labels = {"name": QLabel(self), "rating": QLabel(self)}
        self.labels["name"].move(120, 0)
        self.labels["rating"].move(120, 40)

        # кнопка редактирования
        self.btn = QPushButton('Edit', self)
        self.btn.resize(100, 40)
        self.btn.move(0, 80)
        # по клику открываю новую форму редактирования
        self.btn.clicked.connect(self.openEditDataForm)

        # Обновим информацию в label'ах
        self.updateView()

        self.show()

    # Метод обновления данных в label'ах. Когда мне нужно, я вызываю этот метод и происходит синхронизация отображаемых
    # в полях данных и моих реальных данных в переменной self.data
    def updateView(self):
        for key in self.data:
            label = self.labels[key]
            label.setText(str(self.data[key]))
            label.adjustSize()

    def saveData(self, data):
        self.data = data
        self.updateView()
        self.second_form.hide()

    # открытие формы редактирования
    def openEditDataForm(self):
        # передаю туда 2 параметра - запись с моими данными (словарь)
        # и функцию/метод, который будет принимать уже отредактированные данные
        self.second_form = SecondForm(self.data, self.saveData)
        self.second_form.setGeometry(200, 200, 200, 200)
        self.second_form.show()


class SecondForm(QWidget):
    def __init__(self, data, save_function):
        super().__init__()
        self.save_function = save_function
        # сделаем "глубокую" копию наших данных, чтобы не испортить данные в родительской форме и они были независимыми
        # на период редактирования
        self.data = copy.deepcopy(data)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Вторая форма')
        # создадим поля ввода под каждое поле нашей записи и соберем их в словарь с такими же ключами
        self.edits = {"name": QLineEdit(self), "rating": QLineEdit(self)}
        self.edits["rating"].move(0, 40)

        self.btn_save = QPushButton(self)
        self.btn_save.setText("Сохранить")
        self.btn_save.move(0, 100)
        self.btn_save.clicked.connect(self.saveData)
        self.updateView()

    # Собираем данные из полей ввода и сохраняем в self.data
    # тут можно использовать промежуточную переменную, если нам важно иметь возможность получить изначальные данные,
    # которые были переданы в форму, но в данном случае у нас такого требования нет
    # так как после сохранения данных форма просто закроется
    def saveData(self):
        for key in self.edits:
            edit = self.edits[key]
            self.data[key] = edit.text()
        # мы собрали данные из полей ввода, сформировали в self.data новую, отредактированную запись
        # передадим отредактированные данные обратно, родителю
        self.save_function(self.data)

    # обновим наши поля ввода - проставим начальные данные, каждому полю нашего словара (нашей записи)
    # соответствует поле ввода
    def updateView(self):
        for key in self.data:
            edit = self.edits[key]
            edit.setText(str(self.data[key]))
            edit.adjustSize()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FirstForm()
    sys.excepthook = except_hook
    ex.show()
    sys.exit(app.exec())
