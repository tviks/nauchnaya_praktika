import random
import sys  # sys нужен для передачи argv в QApplication
import os  # Отсюда нам понадобятся методы для отображения содержимого директорий

from PyQt5 import QtWidgets
import numpy as np
from PyQt5.QtGui import QPixmap
from src.ploter import *
import form # Это наш конвертированный файл дизайна

class ExampleApp(QtWidgets.QMainWindow, form.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.start_btn.clicked.connect(self.start_plot)


    def start_plot(self):
        create_plot('data/1.csv')
        pixmap = QPixmap('png/pic.png')
        self.pic_label.setPixmap(pixmap)
        self.pic_label.setScaledContents(True)
        self.setCentralWidget(self.pic_label)
        self.resize(pixmap.width(), pixmap.height())

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()