# import numpy as np
import cv2
import matplotlib.pyplot as plt


# Загрузка изображения
image = cv2.imread('tiger.jpg', cv2.IMREAD_GRAYSCALE)
res_image = image.copy()
image_pixels = res_image.shape[0] * res_image.shape[1]

# Создание графика
figure = plt.figure(figsize=(6, 4))
figure_1 = plt.figure(figsize=(6, 4))
ax = figure.add_subplot()
ax_1 = figure_1.add_subplot()
hist_cumulative = hist = ax.hist(res_image.ravel(), 256)
hist_data = [i for i in hist[0]]
hist_data_len = len(hist_data)


# Нормализация гистограммы
for i in range(hist_data_len):

    hist[0][i] = int(hist_data[i]) / image_pixels


# Вычисление кумулятивной гистограммы
for i in range(1, hist_data_len):

    hist_cumulative[0][i] = hist[0][i - 1] + hist[0][i]


# Обработка изображения
for i in range(res_image.shape[0]):
    for j in range(res_image.shape[1]):

        res_image[i][j] = 255 * hist_cumulative[0][res_image[i][j]]


hist_result = ax_1.hist(res_image.ravel(), 256)
ax.grid()
ax_1.grid()
plt.show()
cv2.imshow('tiger', res_image)
cv2.waitKey(0)
# cv2.imwrite('roses-result.jpeg', res_image)
