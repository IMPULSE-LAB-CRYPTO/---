import cv2
import numpy as np

img = cv2.imread('image.jpg')  # загрузка изображения

cv2.imshow('girl', img)  # отображение
cv2.waitKey(0)

cv2.imwrite('image2.jpg', img)  # сохранение изображения

img[0, 0, :] = 255  # замена значения пикселя
shape = img.shape  # получение размера
img2 = img.astype(np.uint8)  # преобразование типовв