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

        print()

    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()





# Предположим, что у вас есть список файлов изображений и их абсолютные пути
file_paths = ["path/to/image1.jpg", "path/to/image2.jpg", "path/to/image3.jpg"]
absolute_paths = [os.path.abspath(file_path) for file_path in file_paths]

# Создаем DataFrame с двумя колонками: абсолютный и относительный пути
df = pd.DataFrame({
    'absolute_path': absolute_paths,
    'relative_path': file_paths
})

# Добавляем колонки для высоты, ширины и глубины изображения
heights = []
widths = []
depths = []

for file_path in file_paths:
    image = cv2.imread(file_path)
    height, width, depth = image.shape
    heights.append(height)
    widths.append(width)
    depths.append(depth)

df['height'] = heights
df['width'] = widths
df['depth'] = depths

# Вычисляем статистическую информацию для столбцов размеров изображения
stats = df[['height', 'width', 'depth']].describe()
print(stats)

# Функция для фильтрации DataFrame по максимальной ширине и высоте изображения
def filter_images(max_width, max_height):
    return df[(df['height'] <= max_height) & (df['width'] <= max_width)]

# Добавляем новый столбец с площадью изображения
df['area'] = df['height'] * df['width']

# Сортируем данные по площади изображений
df = df.sort_values(by='area')

# Создаем гистограмму распределения площадей изображений
plt.hist(df['area'], bins=10, edgecolor='black')
plt.title('Распределение площадей изображений')
plt.xlabel('Площадь изображения')
plt.ylabel('Количество изображений')
plt.show()