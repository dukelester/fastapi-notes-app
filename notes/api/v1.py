""" The endpoints file for the notes app """
from fastapi import APIRouter

router = APIRouter(prefix="/notes")


@router.get("/")
def get_notes():
    """ The homepage of the notes app """
    return "notes app created!"
