from fastapi import APIRouter
from app.services.directions_services import getDirectionsService

router = APIRouter()

@router.get("/direction")
def getDirectionController():
    return getDirectionsService()