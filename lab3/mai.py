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








img = cv2.imread('image.jpg')  # загрузка изображения

cv2.imshow('girl', img)  # отображение
cv2.waitKey(0)

cv2.imwrite('image2.jpg', img)  # сохранение изображения

img[0, 0, :] = 255  # замена значения пикселя
shape = img.shape  # получение размера
img2 = img.astype(np.uint8)  # преобразование типов



plt.imshow(img)  # загрузка изображения
plt.show()  # отображение

# создание данных
x = np.linspace(0, 10, 100)  # 100 точек от 0 до 10
y = np.sin(x)  # нахождение синуса

# создание графика
plt.figure(figsize=(10, 5))  # размер графика

plt.plot(x, y, label='sin(x)', color='blue')  # линейный график синуса
plt.title('График синуса')  # заголовок графика
plt.xlabel('x')  # подпись оси x
plt.ylabel('sin(x)')  # подпись оси y
plt.axhline(0, color='black',linewidth=0.5, ls='--')  # линия по оси x
plt.axvline(0, color='black',linewidth=0.5, ls='--')  # линия по оси y
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)  # сетка
plt.legend()  # легенда

# отображение графика
plt.show()