import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from map_utils import get_coordinates, get_map_params_with_pts


class PharmacyMapApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Аптеки на карте")
        self.setGeometry(100, 100, 900, 700)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        input_layout = QHBoxLayout()
        self.address_input = QLineEdit()
        self.address_input.setPlaceholderText("Введите адрес для поиска аптек")
        self.search_button = QPushButton("Найти аптеки")
        self.search_button.clicked.connect(self.find_pharmacies)
        input_layout.addWidget(self.address_input)
        input_layout.addWidget(self.search_button)
        layout.addLayout(input_layout)

        self.status_label = QLabel("Введите адрес и нажмите 'Найти аптеки'")
        layout.addWidget(self.status_label)

        self.map_label = QLabel()
        self.map_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.map_label)

    def get_pharmacies(self, lon, lat):
        api_key = "dda3ddba-c9ea-4ead-9010-f43fbc15c6e3"
        url = "https://search-maps.yandex.ru/v1/"
        params = {
            "apikey": api_key,
            "text": "аптека",
            "ll": f"{lon},{lat}",
            "type": "biz",
            "results": 10
        }

        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json().get("features", [])
        return []

    def get_pharmacy_color(self, hours):
        if not hours:
            return "gray"
        hours_lower = hours.lower()
        if "24" in hours_lower or "круглосуточно" in hours_lower:
            return "green"
        return "blue"

    def find_pharmacies(self):
        address = self.address_input.text()
        if not address:
            self.status_label.setText("Введите адрес")
            return

        coordinates = get_coordinates(address)
        if not coordinates:
            self.status_label.setText("Адрес не найден")
            return

        lon, lat = coordinates
        pharmacies = self.get_pharmacies(lon, lat)

        if not pharmacies:
            self.status_label.setText("Аптеки не найдены")
            return

        pts = []
        for pharmacy in pharmacies:
            coords = pharmacy["geometry"]["coordinates"]
            ph_lon, ph_lat = coords
            props = pharmacy["properties"]
            hours = props.get("CompanyMetaData", {}).get("Hours", {}).get("text", None)
            color = self.get_pharmacy_color(hours)
            pts.append(f"{ph_lon},{ph_lat},pm2{color}l")

        params = get_map_params_with_pts([lon, lat], pts)
        response = requests.get("https://static-maps.yandex.ru/1.x/", params=params)

        if response.status_code == 200:
            pixmap = QPixmap()
            pixmap.loadFromData(response.content)
            self.map_label.setPixmap(pixmap)
            self.status_label.setText(f"Найдено аптек: {len(pharmacies)} (зеленые - круглосуточные, синие - нет, серые - нет данных)")
        else:
            self.status_label.setText("Ошибка загрузки карты")


def main():
    app = QApplication(sys.argv)
    window = PharmacyMapApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
