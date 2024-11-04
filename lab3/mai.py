import cv2
import numpy as np
import matplotlib.pyplot as plt
import argparse

def parsing() -> argparse.Namespace:
    """
    Парсинг аргументов командной строки
    """
    parser = argparse.ArgumentParser(description="Работа с изображением")
    parser.add_argument('download_image', type = str, help='path to the input image')
    parser.add_argument('result_image', type = str, help='path to the output image')
    args = parser.parse_args()
    return args

def read_image(input_image, greyscale):
    """
    Чтение изображения из файла
    """
    image = cv2.imread(input_image, greyscale)
    if image is None:
        raise FileExistsError
    return image








def main():
    args = parsing()
    try:
        image = read_image(args.input_image, cv2.IMREAD_GRAYSCALE)
        print(image)


    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()