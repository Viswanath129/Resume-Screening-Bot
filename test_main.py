from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_analyze():
    response = client.post("/analyze", json={
        "job_description": "We need a Python developer.",
        "resumes": [{"id": 1, "name": "Alice", "text": "I am a Python developer."}]
    })
    assert response.status_code == 200
    data = response.json()
    assert "ranked_resumes" in data
    assert len(data["ranked_resumes"]) == 1

def test_analyze_empty():
    response = client.post("/analyze", json={
        "job_description": "",
        "resumes": []
    })
    assert response.status_code == 200
    data = response.json()
    assert "ranked_resumes" in data
    assert len(data["ranked_resumes"]) == 0
