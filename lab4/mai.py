import argparse

import pandas as pd
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

def get_image_dimensions(path:str) -> tuple[int, int, int]:
    '''
    Функция для получения размеров изображения
    :param path: path_to_image
    :return: height, width, depth
    '''
    image = cv2.imread(path)
    if image is not None:
        height, width, depth = image.shape
        return height, width, depth
    else:
        return None, None, None

def add_columns(df:pd.DataFrame) -> None:
    '''
    Добавление столбцов с размерами изображения
    :param df: pandas DataFrame (object)
    :return: None
    '''
    heights = []
    widths = []
    depths = []

    for path in df['absolute_path']:
        height, width, depth = get_image_dimensions(path)
        heights.append(height)
        widths.append(width)
        depths.append(depth)

    df['height'] = heights
    df['width'] = widths
    df['depth'] = depths
    return None

def filter_images(df:pd.DataFrame, max_width:int, max_height:int) -> pd.DataFrame:
    '''
    Функция фильтрации изображений
    :param df:
    :param max_width: width filter
    :param max_height: height filter
    :return: pandas DataFrame (object)
    '''
    return df[(df['height'] <= max_height) & (df['width'] <= max_width)]


def add_column_area(df:pd.DataFrame) -> None:
    '''
    Функция добавления столбца area
    :param df: pandas DataFrame (object)
    :return: None
    '''
    df['area'] = df['height'] * df['width']
    return  None

def gistogramm(df:pd.DataFrame) -> None:
    '''
    Функция создания гистограммы распределения площадей изображений
    :param df: pandas DataFrame (object)
    :return: None
    '''
    plt.hist(df['area'], bins=10, edgecolor='black')
    plt.title('Распределение площадей изображений')
    plt.xlabel('Площадь изображения')
    plt.ylabel('Количество изображений')
    plt.show()
    return None

def main():
    args = parsing()
    try:
        df = pd.read_csv(args.path_to_csv_file)  # загрузка данных из csv файла
        print(df.head())
        print(df.dtypes)
        print("DataFrame создан на основе csv-файла\n")

        add_columns(df)
        print(df.head())
        print("Колонки width, height, depth добавлены\n")

        #
        stats = df[['height', 'width', 'depth']].describe()
        print(stats)
        print("Статистическая информация для столбцов размеров изображения вычислена\n")

        filtered_df = filter_images(df, 500, 500)
        print(filtered_df)
        print("Отфильтрованный DataFrame Выведен\n")

        add_column_area(df)
        print(df.head())
        print("Колонка area добавлена\n")

        df = df.sort_values(by='area')
        print("Сортировка данных по площади изображения\n")

        gistogramm(df)
        print("Гистограмма выведена")

    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()


