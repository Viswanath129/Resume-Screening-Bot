import requests

data = {
    "job_description": "We need a Python developer.",
    "resumes": [
        {
            "id": 1,
            "name": "John",
            "text": "I am a Python developer."
        }
    ]
}
response = requests.post("http://127.0.0.1:8000/analyze", json=data)
print(response.json())
