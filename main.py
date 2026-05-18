import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import requests
from map_utils import get_map_params, get_object_coordinates, get_object_size


class MapApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Поиск объектов на карте")
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        input_layout = QHBoxLayout()
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Введите адрес или объект для поиска")
        self.search_button = QPushButton("Найти")
        self.search_button.clicked.connect(self.search_object)
        input_layout.addWidget(self.search_input)
        input_layout.addWidget(self.search_button)
        layout.addLayout(input_layout)

        self.map_label = QLabel()
        self.map_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.map_label)

    def search_object(self):
        query = self.search_input.text()
        if not query:
            return

        coordinates = get_object_coordinates(query)
        if not coordinates:
            self.map_label.setText("Объект не найден")
            return

        size = get_object_size(coordinates[0], coordinates[1], query)

        params = get_map_params(coordinates, size)

        response = requests.get("https://static-maps.yandex.ru/1.x/", params=params)

        if response.status_code == 200:
            pixmap = QPixmap()
            pixmap.loadFromData(response.content)
            self.map_label.setPixmap(pixmap)
        else:
            self.map_label.setText("Ошибка загрузки карты")


def main():
    app = QApplication(sys.argv)
    window = MapApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()