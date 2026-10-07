import PyPDF2
from reportlab.pdfgen import canvas
import requests
import os

# Create a mock PDF
pdf_path = "mock.pdf"
c = canvas.Canvas(pdf_path)
c.drawString(100, 750, "This is a test PDF document.")
c.save()

# Start testing
with open(pdf_path, "rb") as f:
    files = {"files": (pdf_path, f, "application/pdf")}
    try:
        response = requests.post("http://localhost:8000/upload", files=files)
        print("Status Code:", response.status_code)
        print("Response:", response.json())
    except Exception as e:
        print("Error connecting to server:", e)

# Cleanup
os.remove(pdf_path)
