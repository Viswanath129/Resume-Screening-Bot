# Resume-Screening-Bot
Intelligent ranking tool using TF-IDF and embeddings to score candidates against job descriptions. Deployed via FastAPI &amp; Streamlit.
Resume Screening Bot

An intelligent NLP-based tool that ranks candidate resumes against a job description using TF-IDF Vectorization and Cosine Similarity.

Architecture

Backend: FastAPI (Handles the logic/ML)

Frontend: Streamlit (Handles the UI and File Uploads)

Algorithm: TF-IDF (Term Frequency-Inverse Document Frequency) + Cosine Similarity

Setup Instructions

1. Prerequisites

Python 3.8 or higher installed.

2. Installation

Create a virtual environment and install dependencies:

# Create virtual env
python -m venv venv

# Activate (Windows)
venv\Scripts\activate
# Activate (Mac/Linux)
source venv/bin/activate

# Install requirements
pip install -r requirements.txt
--
fastapi
uvicorn
streamlit
scikit-learn
pydantic
PyPDF2
requests
python-multipart
----


3. Running the Application

You need to run the Backend and Frontend in two separate terminal windows.

Terminal 1: Start Backend (FastAPI)

python main.py
# Server will start at http://localhost:8000


Terminal 2: Start Frontend (Streamlit)

streamlit run app.py
# Browser will open at http://localhost:8501


📝 Usage

Open the Streamlit URL.

Paste a Job Description in the left panel.

Upload one or more Resumes (PDF or TXT) in the right panel.

Click Analyze.

View the ranked list of candidates based on how well their resume text matches the job description keywords.
