from fastapi import APIRouter
from ..controllers.directions_controllers import getDirectionController

# router = APIRouter(prefix="/directions",tags=["directions"],)
router = APIRouter()

@router.get("/")
# @router.get("/direction")
def read_direction():
    return getDirectionController()