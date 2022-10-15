""" Testing file for the main file """

def test_main(test_app):
    """ Testing the main file """
    response = test_app.get("/")
    assert response.status_code == 200
    assert response.json() == {"success": " Welcome to the notes application with FastAPI."}
