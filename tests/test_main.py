""" Testing file for the main file """

from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)

def test_main():
    """ Testing the main file """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"success": " Welcome to the notes application with FastAPI."}
