# import numpy as np
import cv2
import matplotlib.pyplot as plt


# Загрузка изображения
image = cv2.imread('roses.jpeg', cv2.IMREAD_GRAYSCALE)
res_image = cv2.resize(image, (int(image.shape[0] / 2), int(image.shape[1] / 2)))
image_pixels = res_image.shape[0] * res_image.shape[1]

# Создание графика
figure = plt.figure(figsize=(6, 4))
ax = figure.add_subplot()
biba = ax.hist(res_image.ravel(), 256)
biba_zalupa = [i for i in biba[0]]
biba_len = len(biba[0])

# Нормализация гистограммы
for i in range(biba_len):

    biba_zalupa[i] = int(biba[0][i]) / image_pixels

# Обработка изображения
for i in range(res_image.shape[0]):
    for j in range(res_image.shape[1]):

        res_image[i][j] = 20 * 255 * biba_zalupa[res_image[i][j]]

# cv2.imshow('image', image)
# cv2.waitKey(0)
# print(len(biba[0]))
ax.grid()
plt.show()
cv2.imshow('tiger', res_image)
cv2.waitKey(0)


figure_1 = plt.figure(figsize=(6, 4))
ax_1 = figure_1.add_subplot()
