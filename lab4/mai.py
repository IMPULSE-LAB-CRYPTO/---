import argparse

import pandas as pd
import cv2
import matplotlib.pyplot as plt

from images_module import get_image_dimensions, add_column_area, add_columns, filter_images

def parsing() -> argparse.Namespace:
    """
    Парсинг аргументов командной строки
    """
    parser = argparse.ArgumentParser(description="Работа с изображением")
    parser.add_argument('path_to_images_folder', type = str, help='path to folder with images')
    parser.add_argument('path_to_csv_file', type=str, help='path to the csv file')
    args = parser.parse_args()
    return args


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

        df_sort = df.sort_values(by='area')
        print((df_sort))
        print("Сортировка данных по площади изображения\n")

        gistogramm(df)
        print("Гистограмма выведена")

    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()


