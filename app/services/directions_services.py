from app.repositories.direction_repo import dbGetDirection

def getDirectionsService():
    directions = dbGetDirection()
    return directions