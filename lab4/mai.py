import argparse
import csv

import pandas as pd  # импорт


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


def main():
    args = parsing()
    try:
        df = pd.read_csv("data.csv")  # загрузка данных из csv файла
        print(df.head())  # отображение первых строк таблицы


    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()