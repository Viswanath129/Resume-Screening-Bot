from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_analyze():
    response = client.post("/analyze", json={
        "job_description": "We need a Python developer.",
        "resumes": [
            {"id": 1, "name": "Alice", "text": "Python developer with 5 years of experience."}
        ]
    })
    assert response.status_code == 200
    data = response.json()
    assert "ranked_resumes" in data
    assert len(data["ranked_resumes"]) == 1
