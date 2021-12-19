"""
READ_LOCATION

Funciones relacionadas a encontrar datos de una ubicación especifica. 

@author: ecastaneda
"""

import certifi
import ssl
import geopy.geocoders
from geopy.geocoders import Nominatim

def get_location_data(latitude: float, longitude: float) -> str:
    """A partir de coordenadas identifica el nombre del lugar.

    Args:
        latitude (float): Latitud del dispositivo.
        longitude (float): Longitud del dispositivo.

    Returns:
        str: Nombre del lugar.
    """
    # Inicializar certificado para consulta
    ctx = ssl.create_default_context(cafile=certifi.where())
    geopy.geocoders.options.default_ssl_context = ctx
    # Configurar consulta
    locator = Nominatim(user_agent="my-app")
    # Realizar consulta
    coordinates = f"{latitude}, {longitude}"
    location = locator.reverse(coordinates)
    address = location.address
    return address
 
if __name__ == "__main__":
    test_coordinates = 25.66929326376954, -100.30992600552389
    get_location_data(test_coordinates[0], test_coordinates[1])