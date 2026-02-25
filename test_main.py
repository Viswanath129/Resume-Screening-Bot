from fastapi.testclient import TestClient
from main import app, get_tokens, clean_text

client = TestClient(app)

def test_clean_text():
    assert clean_text("Hello World!") == "hello world"
    assert clean_text("Python 3.9 is Awesome@#$") == "python  is awesome"

def test_get_tokens():
    text = "The quick brown fox jumps over the lazy dog."
    # 'quick', 'brown', 'jumps', 'lazy' (dog, fox, the, over are stopwords or too short?)
    # "dog", "fox" have len 3. "the", "over" are stopwords.
    tokens = get_tokens(text)
    assert "quick" in tokens
    assert "brown" in tokens
    assert "jumps" in tokens
    assert "lazy" in tokens
    assert "the" not in tokens
    assert "fox" in tokens  # len is 3, stopword? 'fox' is not a stopword.
    assert "dog" in tokens  # len is 3

def test_analyze_endpoint():
    payload = {
        "job_description": "Python developer with FastAPI experience.",
        "resumes": [
            {
                "id": 1,
                "name": "Candidate A",
                "text": "I am a Python developer and I know FastAPI.",
                "score": 0,
                "matches": [],
                "missing": []
            },
            {
                "id": 2,
                "name": "Candidate B",
                "text": "I am a Java developer.",
                "score": 0,
                "matches": [],
                "missing": []
            }
        ]
    }
    response = client.post("/analyze", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert len(data["ranked_resumes"]) == 2
    # Candidate A should have a higher score (or at least positive)
    assert data["ranked_resumes"][0]["name"] == "Candidate A"
    assert data["ranked_resumes"][0]["score"] > data["ranked_resumes"][1]["score"]
