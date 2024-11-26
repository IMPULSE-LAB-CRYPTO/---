import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QFileDialog, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap

from module import ImageIterator


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # Вызов инициализатора род класса QMainWindow
        self.setWindowTitle("Просмотр датасета")

        self.image_label = QLabel(self)  # объект QLabel(приложение графический интерфейса GUI)
        self.image_label.setFixedSize(800, 600)

        self.next_button = QPushButton("Следующее изображение", self)
        self.next_button.clicked.connect(self.show_next_image)  # Подключение обработчика события clicked к методу show

        self.open_button = QPushButton("Выбрать папку датасета", self)
        self.open_button.clicked.connect(self.open_dataset_folder)

        # Создаем вертикальный макет и добавляем в него кнопки
        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        layout.addWidget(self.next_button)
        layout.addWidget(self.open_button)

        # Создаем виджет-контейнер и устанавливаем для него макет
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        self.iterator = None

    def open_dataset_folder(self) -> None:
        folder_path = QFileDialog.getExistingDirectory(self, "Выберите папку с датасетом")
        if folder_path:
            self.iterator = ImageIterator(folder_path=folder_path)
            if len(self.iterator.images) == 0:
                self.image_label.setText("Изображений нет в папке")
                return None
            # Открытие изображения сразу
            next_image_path = next(self.iterator)
            pixmap = QPixmap(next_image_path)
            self.image_label.setPixmap(pixmap.scaled(self.image_label.size(), aspectRatioMode=1))

    def show_next_image(self) -> None:
        if self.iterator and len(self.iterator.images) != 0:
            try:
                next_image_path = next(self.iterator)
                pixmap = QPixmap(next_image_path)  # QPixmap содержит всю информацию о пикселях изображения (их цвет и позицию)
                self.image_label.setPixmap(pixmap.scaled(self.image_label.size(), aspectRatioMode=1)) # Установка пиксельной карты в окно. aspectRatioMode - сохраняет пропорции
            except StopIteration:
                self.image_label.setText("Больше изображений нет")


def main():
    try:
        app = QApplication(sys.argv)
        window = MainWindow()  # Создаем свой класс
        window.show()  # Вывод окна на экран
        sys.exit(app.exec_())  # Устанавливаем закрытие окна только после события нажатия на крестик

    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()