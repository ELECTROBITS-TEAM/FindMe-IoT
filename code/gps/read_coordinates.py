"""
READ_COORDINATES

Librería para lectura de coordenadas.

@author: ecastaneda
"""

def get_coordinates() -> tuple:
    """Determina coordenadas de dispositivo.

    Returns:
        tuple: latitud, longitud.
    """
    # TODO: read coordinates from sensor to replace dummy coordinates
    latitude, logitude = dummy_coordinates()


def dummy_coordinates() -> tuple:
    """Regresa coordenadas de prueba.

    Returns:
        tuple: latitud, logintud.
    """
    latitude = 25.669287203700236
    longitude = -100.30994076079043
    return latitude, longitude