import sys
# https://pypi.org/project/audioplayer/ документация
# поддерживает основные операции:
# запуск воспроизведения - play
# пауза - pause()
# возобновление после паузы - resume()
# полная остановка воспроизведения - stop()
# "выгрузка"/освобождение файла - close () - воспроизведение после этого будет невозможно запустить заново
from audioplayer import AudioPlayer
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QComboBox
from PyQt5.QtWidgets import QMainWindow, QLabel


class FirstForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.button = QPushButton(self)
        self.button.setText("На паузу")
        # флаг, с помощью которого мы будем узнавать, на паузе ли наше аудио. Изначально False - аудио воспроизводится
        self.is_pause = False
        self.button.clicked.connect(self.pause)
        # аудиоплейер
        self.player = AudioPlayer("file_example_MP3_700KB.mp3")
        # можно установить громкость с помощью self.player.volume(n), где n целое число от 0 до 100

        # запускаем воспроизведение
        self.player.play()

    def pause(self):
        # аудио на паузе? значит надо возобновить воспроизведение
        if self.is_pause:
            self.player.resume()
            self.button.setText("На паузу")
        # аудио не на паузе - поставим на паузу
        else:
            self.button.setText("Возобновить")
            self.player.pause()
        # меняем флаг паузы на противоположный
        # соответственно, если аудио было на паузе - флаг станет False, если не было - станет True
        self.is_pause = not self.is_pause

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Главная форма')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FirstForm()
    ex.show()
    sys.exit(app.exec())
