import unittest
from fastapi.testclient import TestClient
from main import app, get_tokens, clean_text

class TestResumeApp(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_clean_text(self):
        self.assertEqual(clean_text("Hello World! 123"), "hello world ")
        self.assertEqual(clean_text("Python & Java"), "python  java")

    def test_get_tokens(self):
        tokens = get_tokens("This is a sample text with Python and Java.")
        self.assertIn("python", tokens)
        self.assertIn("java", tokens)
        self.assertNotIn("this", tokens) # stopword
        self.assertNotIn("is", tokens) # stopword

    def test_analyze_endpoint(self):
        payload = {
            "job_description": "We need a Python developer with Flask experience.",
            "resumes": [
                {
                    "id": 1,
                    "name": "Candidate 1",
                    "text": "I am a Python developer with Flask and Django experience.",
                    "score": 0,
                    "matches": [],
                    "missing": []
                },
                {
                    "id": 2,
                    "name": "Candidate 2",
                    "text": "I am a Java developer with Spring experience.",
                    "score": 0,
                    "matches": [],
                    "missing": []
                }
            ]
        }
        response = self.client.post("/analyze", json=payload)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("ranked_resumes", data)
        self.assertEqual(len(data["ranked_resumes"]), 2)
        # Verify sorting (Candidate 1 should be first as it matches Python/Flask)
        self.assertEqual(data["ranked_resumes"][0]["name"], "Candidate 1")

if __name__ == '__main__':
    unittest.main()
