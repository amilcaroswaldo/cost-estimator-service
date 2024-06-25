from fastapi import FastAPI
from app.controllers.directions_controllers import router
from app.statics.constants import APIFORMAT
from fastapi.middleware.cors import CORSMiddleware
nameTag = 'templates_products'
urlAPI = f'{APIFORMAT}/{nameTag}'

def create_app() -> FastAPI:
    app = FastAPI()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(router, prefix=urlAPI, tags=[nameTag])
    return app
