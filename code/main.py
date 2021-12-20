from gps.read_coordinates import get_coordinates
from gps.read_location import get_location_data


def messenger():
    # Consulta de coordenadas
    print("Consulta de coordenadas")
    latitude, longitude = get_coordinates()
    print(f"Coordenadas: {latitude}, {longitude}")
    # Consulta de ubicación
    location_name = get_location_data(latitude, longitude)
    print(f"Ubicación: {location_name}")


if __name__ == "__main__":
    messenger()