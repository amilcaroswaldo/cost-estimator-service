from ..repositories.direction_repo import dbGetDirection

def getDirectionsService():
    directions = dbGetDirection()
    # Aplica la lógica de negocio aquí si es necesario
    return directions