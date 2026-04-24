from fastapi.testclient import TestClient
from main import app
import unittest.mock as mock

client = TestClient(app)

def test_analyze_resumes_exception_leakage():
    # Mock TfidfVectorizer to raise an exception, as it's called inside the try block
    with mock.patch("main.TfidfVectorizer", side_effect=Exception("Secret internal error details!")):
        response = client.post(
            "/analyze",
            json={
                "job_description": "Software Engineer",
                "resumes": [
                    {"id": 1, "name": "Alice", "text": "Python developer"}
                ]
            }
        )
        assert response.status_code == 500
        assert response.json()["detail"] == "An internal server error occurred."
        assert "Secret internal error details!" not in response.text
