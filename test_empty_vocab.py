import requests

data = {
    "job_description": "We need a Python developer.",
    "resumes": [
        {
            "id": 1,
            "name": "Empty Resume",
            "text": "the a is and"
        }
    ]
}
response = requests.post("http://127.0.0.1:8000/analyze", json=data)
print(response.json())
