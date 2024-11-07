import numpy as np
import cv2
import matplotlib.pyplot as plt

def write_image(input_image, greyscale) -> np.ndarray:
    """
    Запись нового изображения в файл
    :param input_image: входное изображение
    :param greyscale: аргумент для обработки серых изображений
    :return:  Mat | ndarray[Any, dtype] | ndarray
    """
    image = cv2.imread(input_image, greyscale)
    if image is None:
        raise FileExistsError
    return image


def gistogramm(image) -> None:
    """
    Функция для построения и отображения гистограммы изображения
    :param image: Изображение для построение гистограммы
    :return: None
    """
    plt.figure()
    plt.title("Grayscale Histogram")
    plt.xlabel("Bins")
    plt.ylabel("# of Pixels")
    # Аргументы: 1-само изображение 2-канал(серый,зеленый,синий) 3-mask(срез),
    # 4-количество интервалов, 5-диапозон на графике
    hist = cv2.calcHist([image], [0], None, [256], [0, 256])
    plt.plot(hist)
    plt.xlim([0, 256])
    plt.show()


def task_binary_image(image) -> np.ndarray:
    """
    Преобразование в бинарное изображение
    :param image:
    :return: многомерный массив
    """
    '''
    Аргументы: 1-само изображение 2-пороговое значение(ниже пиксели черные, выше-белые)
    3-значение присвоенное пикселям прошедшим порог 4-бинарное преобразование
    '''
    _, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
    return binary_image