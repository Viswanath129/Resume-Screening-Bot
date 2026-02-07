
from fastapi.testclient import TestClient
from main import app, clean_text, get_tokens
import nltk
from nltk.corpus import stopwords

client = TestClient(app)

# Ensure nltk is downloaded
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

def test_clean_text():
    # regex: re.sub(r'[^a-zA-Z\s]', '', text)
    assert clean_text("Hello World!") == "hello world"
    assert clean_text("Python 3.9") == "python "
    # \s matches whitespace characters including \n and \t
    assert clean_text("Line\nBreak") == "line\nbreak"

def test_get_tokens():
    text = "The quick brown fox jumps over the lazy dog."
    tokens = get_tokens(text)

    # Check common non-stopwords
    assert "quick" in tokens
    assert "brown" in tokens

    # Check stopwords
    assert "the" not in tokens
    assert "over" not in tokens

    # Check length filtering (len > 2)
    assert "is" not in get_tokens("This is a test")
    assert "at" not in get_tokens("at home")

def test_analyze_endpoint():
    payload = {
        "job_description": "We need a Python developer with FastAPI and React experience.",
        "resumes": [
            {
                "id": 1,
                "name": "Candidate 1",
                "text": "I am a Python developer with FastAPI experience.",
                "score": 0,
                "matches": [],
                "missing": []
            },
            {
                "id": 2,
                "name": "Candidate 2",
                "text": "I write Java code.",
                "score": 0,
                "matches": [],
                "missing": []
            }
        ]
    }
    response = client.post("/analyze", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "ranked_resumes" in data
    assert len(data["ranked_resumes"]) == 2

    # Check ranking (Candidate 1 should be higher)
    resumes = data["ranked_resumes"]
    assert resumes[0]["id"] == 1
    assert resumes[0]["score"] > resumes[1]["score"]

    # Check matches
    matches = resumes[0]["matches"]
    assert "python" in matches
    assert "fastapi" in matches
