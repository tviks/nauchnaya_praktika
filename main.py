import sys  # sys нужен для передачи argv в QApplication
import os  # Отсюда нам понадобятся методы для отображения содержимого директорий

from PyQt5 import QtWidgets
from src.ploter import *
import ui  # Это наш конвертированный файл дизайна

class ExampleApp(QtWidgets.QMainWindow, ui.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.folder_btn.clicked.connect(self.browse_folder)  # Выполнить функцию browse_folder
        self.plot_btn.clicked.connect(self.show_plot)
        self.file_list.itemDoubleClicked.connect(self.item_select)

    def show_plot(self, file_name):
        create_plot('data/'+file_name)
        pixmap = QPixmap('png/pic.png')
        self.pic_lable.setPixmap(pixmap)
        self.pic_lable.setScaledContents(True)
        #self.setCentralWidget(self.pic_lable)
        #self.resize(pixmap.width(), pixmap.height())
        
    def browse_folder(self):
        self.file_list.clear()  # На случай, если в списке уже есть элементы
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку")
        # открыть диалог выбора директории и установить значение переменной
        # равной пути к выбранной директории

        if directory:  # не продолжать выполнение, если пользователь не выбрал директорию
            for file_name in os.listdir(directory):  # для каждого файла в директории
                self.file_list.addItem(file_name)   # добавить файл в listWidget
    
        
    def item_select(self):
        item = self.file_list.currentItem()
        if item is not None:
            print(item.text())
            self.show_plot(file_name=item.text())
        return(item.text())

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()