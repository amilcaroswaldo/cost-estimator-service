from fastapi import FastAPI
from app.routers import directions_routers

app = FastAPI()

app.include_router(directions_routers.router)