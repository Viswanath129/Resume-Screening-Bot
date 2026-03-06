from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_analyze():
    response = client.post(
        "/analyze",
        json={
            "job_description": "We are looking for a Python developer with experience in FastAPI and Machine Learning. Must know SQL and React.",
            "resumes": [
                {
                    "id": 1,
                    "name": "Ramesh",
                    "text": "Experienced Python developer with a background in Flask and Django. Familiar with SQL and basic ML concepts.",
                    "score": 0,
                    "matches": [],
                    "missing": []
                },
                {
                    "id": 2,
                    "name": "Swathi",
                    "text": "Project Manager with 5 years experience in Agile and Scrum. Good communication skills.",
                    "score": 0,
                    "matches": [],
                    "missing": []
                }
            ]
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert "ranked_resumes" in data
    assert len(data["ranked_resumes"]) == 2
    assert data["ranked_resumes"][0]["name"] == "Ramesh"
    assert data["ranked_resumes"][0]["score"] > data["ranked_resumes"][1]["score"]
