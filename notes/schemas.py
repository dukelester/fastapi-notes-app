""" The pydantic schemas for the notes app """

from pydantic import BaseModel, constr, validator

class NotesSchema(BaseModel):
    """ Schema model
    This is the schema for the notes model which takes the title
    and the description of the notes.
    """
    title: constr(max_length=100)
    description: str

    @validator("title", pre=True)
    @classmethod
    def validate_title(cls, title):
        """ Validate the title"""
        if len(title) > 100:
            raise ValueError("The title should be less than 100 characters")
        if len(title) < 5:
            raise ValueError("The title too short")
        return title.capitalize()

    @validator("description", pre=True)
    @classmethod
    def validate_description(cls, description):
        """ Validate the title"""
        if len(description) < 10:
            raise ValueError("The description is too short")
        return description.title()
