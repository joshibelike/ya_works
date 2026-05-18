import requests


def get_coordinates(address):
    geocode_url = "http://geocode-maps.yandex.ru/1.x/"
    params = {
        "apikey": "8013b162-6b42-4997-9691-77b7074026e0",
        "geocode": address,
        "format": "json"
    }

    response = requests.get(geocode_url, params=params)

    if response.status_code == 200:
        data = response.json()
        try:
            point = data["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"]
            lon, lat = map(float, point.split())
            return [lon, lat]
        except (IndexError, KeyError):
            return None
    return None


def get_map_params_with_pts(center, pts, spn=None):
    lon, lat = center

    if spn is None:
        spn = [0.05, 0.05]

    params = {
        "ll": f"{lon},{lat}",
        "spn": f"{spn[0]},{spn[1]}",
        "l": "map",
        "pt": "~".join(pts)
    }
    return params
