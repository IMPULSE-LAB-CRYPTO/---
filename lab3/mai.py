import cv2
import numpy as np
import matplotlib.pyplot as plt
import argparse

def parsing() -> argparse.Namespace:
    """
    Парсинг аргументов командной строки
    """
    parser = argparse.ArgumentParser(description="Работа с изображением")
    parser.add_argument('path_to_download_image', type = str, help='path to the input image')
    parser.add_argument('path_to_result_image', type = str, help='path to the output image')
    args = parser.parse_args()
    return args

def write_image(input_image, greyscale):
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
    hist = cv2.calcHist([image], [0], None, [256], [0, 256])
    plt.plot(hist)
    plt.xlim([0, 256])
    plt.show()

def task_binary_image(image):
    """
    Преобразование в бинарное изображение
    :param image:
    :return:
    """
    # Преобразование изображения в бинарное
    _, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
    return binary_image


def main():
    args = parsing()
    try:
        image = write_image(args.path_to_download_image, cv2.IMREAD_GRAYSCALE)
        cv2.imshow('Arcane', image)
        cv2.waitKey(0)

        # Вывод размера изображения
        shape = image.shape
        print(f"Размер изображения: {shape}")

        # Построение и отображение гистограммы
        gistogramm(image)





    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()