""" The main entry to the project """

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from notes.api import v1
from app.core.config import settings
from .database import SessionLocal

def get_db():
    """ a function to create the database """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

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
    get_db()

    return _app

app = get_application()


@app.on_event("startup")
async def startup():
    """ The database connection established during startup """
    print("***** Welcome \n database connection success ****")

@app.on_event("shutdown")
async def shutdown():
    """ Shutdown the application and disconnet the database """
    print("***** Database disconnected successfully!! ****")

@app.get("/")
async def index():
    """ A simple home page view """
    return {"success": " Welcome to the notes application with FastAPI."}
