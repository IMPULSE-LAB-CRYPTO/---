import argparse

import pandas as pd
import os
import cv2
import matplotlib.pyplot as plt

def parsing() -> argparse.Namespace:
    """
    Парсинг аргументов командной строки
    """
    parser = argparse.ArgumentParser(description="Работа с изображением")
    parser.add_argument('path_to_images_folder', type = str, help='path to folder with images')
    parser.add_argument('path_to_csv_file', type=str, help='path to the csv file')
    args = parser.parse_args()
    return args

def get_image_dimensions(path):
    '''
    Функция для получения размеров изображения
    :param path:
    :return: height, width, depth
    '''
    image = cv2.imread(path)
    if image is not None:
        height, width, depth = image.shape
        return height, width, depth
    else:
        return None, None, None

def add_columns(df):
    '''
    Добавление столбцов с размерами изображения
    :return: None
    '''
    # Создание пустых списков для размеров изображений
    heights = []
    widths = []
    depths = []

    # Заполнение списков размерами изображений
    for path in df['absolute_path']:
        height, width, depth = get_image_dimensions(path)
        heights.append(height)
        widths.append(width)
        depths.append(depth)

    # Добавление столбцов с размерами изображений в DataFrame
    df['height'] = heights
    df['width'] = widths
    df['depth'] = depths
    return None

def filter_images(df, max_width, max_height):
    '''
    Функция фильтрации изображений
    :param df:
    :param max_width:
    :param max_height:
    :return:
    '''
    return df[(df['height'] <= max_height) & (df['width'] <= max_width)]


def add_column_area(df):
    '''
    Функция добавления столбца area
    :param df:
    :return: None
    '''
    df['area'] = df['height'] * df['width']
    return  None

def gistogramm(df):
    '''
    Функция создания гистограммы распределения площадей изображений
    :param df:
    :return:
    '''
    plt.hist(df['area'], bins=10, edgecolor='black')
    plt.title('Распределение площадей изображений')
    plt.xlabel('Площадь изображения')
    plt.ylabel('Количество изображений')
    plt.show()

def main():
    args = parsing()
    try:
        df = pd.read_csv(args.path_to_csv_file)  # загрузка данных из csv файла
        print(df.head())
        print()

        add_columns(df)
        print(df.head())

        # Вычисляем статистическую информацию для столбцов размеров изображения
        stats = df[['height', 'width', 'depth']].describe()
        print(stats)
        print()

        add_column_area(df)
        print(df)

        # Сортируем данные по площади изображений
        df = df.sort_values(by='area')

        gistogramm(df)
        print()

    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()


