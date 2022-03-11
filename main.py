# import numpy as np
import cv2
import matplotlib.pyplot as plt


# Загрузка изображения
image = cv2.imread('tiger.jpg', cv2.IMREAD_GRAYSCALE)
image_copy = image.copy()
image_pixels = image.shape[0] * image.shape[1]

# Создание графика
figure = plt.figure(figsize=(6, 4))
ax = figure.add_subplot()
biba = ax.hist(image.ravel(), 256)
biba_zalupa = [i for i in biba[0]]
biba_len = len(biba[0])

# Нормализация гистограммы
for i in range(biba_len):

    biba_zalupa[i] = int(biba[0][i]) / image_pixels

# Обработка изображения
for i in range(image.shape[0]):
    for j in range(image.shape[1]):

        image[i][j] = 255 * biba_zalupa[image[i][j]]

# cv2.imshow('image', image)
# cv2.waitKey(0)
# print(len(biba[0]))
ax.grid()
plt.show()
