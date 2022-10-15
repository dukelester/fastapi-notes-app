""" The main entry to the project """

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings

from notes.api import v1

def get_application():
    """ Get the application """

    _app = FastAPI(title=settings.PROJECT_NAME)

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    _app.include_router(v1.router)

    return _app

app = get_application()

@app.get("/")
async def index():
    """ A simple home page view """
    return {"success": " Welcome to the notes application with FastAPI."}
