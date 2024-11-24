import sys
import argparse
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QFileDialog, QGridLayout, QVBoxLayout, QHBoxLayout, QWidget
from PyQt5.QtGui import QPixmap
from module import ImageIterator

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__() #Вызов инициализатора род класса QMainWindow
        self.setWindowTitle("Просмотр датасета")

        self.image_label = QLabel(self) #Создаем объект
        self.image_label.setFixedSize(800, 600)

        self.prev_button = QPushButton("Прошлое изображение", self)
        self.prev_button.clicked.connect(self.show_prev_image)  # Подключение обработчика события clicked к методу show

        self.next_button = QPushButton("Следующее изображение", self)
        self.next_button.clicked.connect(self.show_next_image)

        self.open_button = QPushButton("Выбрать папку датасета", self)
        self.open_button.clicked.connect(self.open_dataset_folder)

        #Создаем вертикальный макет и добавляем в него кнопки
        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        layout.addWidget(self.prev_button)
        layout.addWidget(self.next_button)
        layout.addWidget(self.open_button)

        #Создаем виджет-контейнер и устанавливаем для него макет
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.iterator = None

    def open_dataset_folder(self) -> None:
        folder_path = QFileDialog.getExistingDirectory(self, "Выберите папку с датасетом")
        if folder_path:
            self.iterator = ImageIterator(None, folder_path)

    def show_next_image(self) -> None:
        if self.iterator:
            try:
                next_image_path = next(self.iterator)
                pixmap = QPixmap(next_image_path)
                self.image_label.setPixmap(pixmap.scaled(self.image_label.size(), aspectRatioMode=1))
            except StopIteration:
                self.image_label.setText("Больше изображений нет")

    #Тест
    def show_prev_image(self) -> None:
        if self.iterator:
            try:
                prev_image_path = next(self.iterator)
                pixmap = QPixmap(prev_image_path)
                self.image_label.setPixmap(pixmap.scaled(self.image_labelsize(), aspectRatioMode=1))

            except StopIteration:
                self.image_label.setText("Больше изображений нет")



def parsing() -> argparse.Namespace:
    """
    Парсинг аргументов командной строки
    """
    parser = argparse.ArgumentParser(description="Работа с изображением")
    parser.add_argument('folder_path', type = str, help='path to the input image')
    args = parser.parse_args()
    return args


def main():
    args = parsing()
    try:
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())


    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()