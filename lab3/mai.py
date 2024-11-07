import argparse

import cv2
import matplotlib.pyplot as plt

from Work_with_images import write_image,gistogramm,task_binary_image


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


def show_all(orig_image, grey_image, binary_image) -> None:
    """
    Функция демонстрации всех трех изображений в одном окне
    :param orig_image: Оригинальное изображение
    :param grey_image: Изображение в диапозоне 256 бит(серое)
    :param binary_image: Бинарное изображение
    :return: None
    """
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
        print(f"Оригинальное изображение сохранено в lab3/orig_image")
        cv2.imshow('Standart_kitty', orig_image)
        cv2.waitKey(0)

        grey_image = write_image(args.path_to_original_image, cv2.IMREAD_GRAYSCALE)
        cv2.imwrite(args.path_to_grey_image, grey_image)
        print(f"Черно-белое изображение сохранено в lab3/grey_image")
        cv2.imshow('Upset_kitty', grey_image)
        cv2.waitKey(0)

        # Вывод размера изображения
        shape = grey_image.shape
        print(f"Размер изображения: {shape}")

        # Построение и отображение гистограммы
        gistogramm(grey_image)

        binary_image = task_binary_image(grey_image)
        cv2.imwrite(args.path_to_binary_image, binary_image)
        print(f"Бинарное изображение сохранено в lab3/binary_image")
        cv2.imshow('black_and_white_kitty', binary_image)
        cv2.waitKey(0)

        # Показываю результат
        show_all(orig_image, grey_image, binary_image)

    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()