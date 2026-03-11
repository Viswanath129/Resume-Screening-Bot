from fastapi.testclient import TestClient
from main import app, ResumeData, AnalysisRequest

client = TestClient(app)

def test_analyze_endpoint():
    request_data = {
        "job_description": "We are looking for a Python developer with React experience.",
        "resumes": [
            {
                "id": 1,
                "name": "Alice",
                "text": "I am a Python developer and I know React and Java."
            },
            {
                "id": 2,
                "name": "Bob",
                "text": "I am a Java developer with spring boot experience."
            }
        ]
    }

    response = client.post("/analyze", json=request_data)

    assert response.status_code == 200
    data = response.json()
    assert "ranked_resumes" in data

    resumes = data["ranked_resumes"]
    assert len(resumes) == 2

    # Alice should score higher than Bob
    assert resumes[0]["name"] == "Alice"
    assert resumes[1]["name"] == "Bob"

    # Check that matches and missing lists are correct length / type
    assert isinstance(resumes[0]["matches"], list)
    assert isinstance(resumes[0]["missing"], list)
    assert isinstance(resumes[0]["score"], float)

def test_analyze_empty():
    request_data = {
        "job_description": "",
        "resumes": []
    }
    response = client.post("/analyze", json=request_data)
    assert response.status_code == 200
    assert response.json() == {"ranked_resumes": []}
