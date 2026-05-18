import requests


def get_object_coordinates(query):
    geocode_url = "http://geocode-maps.yandex.ru/1.x/"
    params = {
        "geocode": query,
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


def get_object_size(lon, lat, query):
    geocode_url = "http://geocode-maps.yandex.ru/1.x/"
    params = {
        "geocode": query,
        "format": "json"
    }

    response = requests.get(geocode_url, params=params)

    if response.status_code == 200:
        data = response.json()
        try:
            envelope = data["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["boundedBy"]["Envelope"]
            lower_corner = envelope["lowerCorner"].split()
            upper_corner = envelope["upperCorner"].split()

            min_lon = float(lower_corner[0])
            min_lat = float(lower_corner[1])
            max_lon = float(upper_corner[0])
            max_lat = float(upper_corner[1])

            size_lon = abs(max_lon - min_lon)
            size_lat = abs(max_lat - min_lat)

            return [size_lon, size_lat]
        except (IndexError, KeyError):
            pass

    return [0.01, 0.01]


def get_map_params(coordinates, size):
    lon, lat = coordinates
    size_lon, size_lat = size

    return {
        "ll": f"{lon},{lat}",
        "spn": f"{size_lon},{size_lat}",
        "l": "map",
        "pt": f"{lon},{lat},pm2rdm"
    }