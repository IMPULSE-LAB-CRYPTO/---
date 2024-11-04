import cv2
import numpy as np
import matplotlib.pyplot as plt
import argparse

def parsing() -> argparse.Namespace:
    """
    Парсинг аргументов командной строки
    """
    parser = argparse.ArgumentParser(description="Работа с изображением")
    parser.add_argument('path_to_original_image', type = str, help='path to the input image')
    parser.add_argument('path_to_grey_image', type=str, help='path to the grey_output image')
    parser.add_argument('path_to_binary_image', type = str, help='path to the binary_output image')
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
    # Аргументы: 1-само изображение 2-канал(серый,зеленый,синий) 3-mask(срез), 4-количество интервалов, 5-диапозон на графике
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

def show_all(orig_image, grey_image, binary_image):

    plt.figure(figsize=(10, 5))

    plt.subplot(1, 3, 1)
    plt.title("Original Image")
    plt.imshow(orig_image, cmap='gray')
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.title("Grey Image")
    plt.imshow(grey_image, cmap='gray')
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.title("Binary Image")
    plt.imshow(binary_image, cmap='gray')
    plt.axis('off')

    plt.show()

def main():
    args = parsing()
    try:
        orig_image = cv2.imread(args.path_to_original_image)

        grey_image = write_image(args.path_to_original_image, cv2.IMREAD_GRAYSCALE)
        cv2.imshow('Kitty', grey_image)
        cv2.waitKey(0)

        cv2.imwrite(args.path_to_binary_image, grey_image)
        print(f"Черно-белое изображение сохранено в lab3/new_image")

        # Вывод размера изображения
        shape = grey_image.shape
        print(f"Размер изображения: {shape}")

        # Построение и отображение гистограммы
        gistogramm(grey_image)

        binary_image = task_binary_image(grey_image)
        cv2.imshow('black_and_white_kitty', binary_image)
        cv2.waitKey(0)

        # Показываю результат
        show_all(orig_image, grey_image, binary_image)




    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()