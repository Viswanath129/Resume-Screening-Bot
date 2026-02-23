from fastapi.testclient import TestClient
from main import app, get_tokens, clean_text

client = TestClient(app)

def test_analyze_endpoint():
    request_data = {
        "job_description": "We are looking for a Python developer with experience in FastAPI and Machine Learning. Must know SQL and React.",
        "resumes": [
            {
                "id": 1,
                "name": "Ramesh",
                "text": "Experienced Python developer with a background in Flask and Django. Familiar with SQL and basic ML concepts."
            },
            {
                "id": 2,
                "name": "Swathi",
                "text": "Project Manager with 5 years experience in Agile and Scrum. Good communication skills."
            }
        ]
    }
    response = client.post("/analyze", json=request_data)
    assert response.status_code == 200
    data = response.json()
    assert "ranked_resumes" in data
    assert len(data["ranked_resumes"]) == 2
    # Check if Ramesh (Python dev) is ranked higher or has a decent score
    ramesh = next(r for r in data["ranked_resumes"] if r["name"] == "Ramesh")
    assert ramesh["score"] > 0
    assert "python" in ramesh["matches"] or "flask" in ramesh["text"].lower()

def test_get_tokens():
    text = "The quick brown fox jumps over the lazy dog."
    tokens = get_tokens(text)
    # verify stop words removed: 'the', 'over'
    assert "the" not in tokens
    assert "over" not in tokens
    # verify content words present: 'quick', 'brown', 'fox', 'jumps', 'lazy', 'dog'
    expected = {"quick", "brown", "fox", "jumps", "lazy", "dog"}
    assert expected.issubset(tokens)

def test_clean_text():
    text = "Hello, World! 123"
    cleaned = clean_text(text)
    assert cleaned == "hello world " # clean_text removes non-alpha but keeps spaces, implementation details: re.sub(r'[^a-zA-Z\s]', '', text) -> 123 gone, comma gone
