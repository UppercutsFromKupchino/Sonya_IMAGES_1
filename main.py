# import numpy as np
import cv2
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget
import matplotlib.pyplot as plt
import sys





class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.button_is_checked = True

        self.setWindowTitle("Matrix 3x3 income/result")

        self.label = QLabel()

        self.input = QLineEdit()
        self.input.setObjectName("host")
        self.input.setText("host")
        self.input.setMaxLength(10)
        self.input.textEdited.connect(self.label.setText)

        self.button3 = QPushButton("Calculate")
        self.button3.clicked.connect(self.calculate)

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)
        layout.addWidget(self.button3)

        container = QWidget()
        container.setLayout(layout)

        # Устанавливаем центральный виджет Window
        self.setCentralWidget(container)

    def set_text(self, text):
        self.label.setText(text)

    def calculate(self):
        text = self.input.text()
        text += '.jpg'
        # Загрузка изображения
        image = cv2.imread(f'{text}', cv2.IMREAD_GRAYSCALE)
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
        cv2.imshow('result', res_image)
        cv2.waitKey(0)


if __name__ == '__main__':
    # Передаём sys.argv, чтобы разрешить аргументы командной строки для приложения
    app = QApplication(sys.argv)

    # Создаём виджет Qt - окно
    window = MainWindow()
    window.show()

    # Цикл событий
    app.exec()
