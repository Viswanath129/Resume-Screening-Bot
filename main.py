import os
import re
import io
from typing import List, Optional
from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.corpus import stopwords
import uvicorn
import PyPDF2

# Download NLTK data (if not present)
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

app = FastAPI(title="Resume Screening Bot")

# CORS Setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development; restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ResumeData(BaseModel):
    id: int
    name: str
    text: str
    score: float = 0
    matches: List[str] = []
    missing: List[str] = []

class AnalysisRequest(BaseModel):
    job_description: str
    resumes: List[ResumeData]

class AnalysisResponse(BaseModel):
    ranked_resumes: List[ResumeData]

# Pre-compile regex and cache stopwords at module level
CLEAN_PATTERN = re.compile(r'[^a-zA-Z\s]')
STOP_WORDS = set(stopwords.words('english'))

def clean_text(text: str) -> str:
    """Cleans text by removing special characters and lowercasing."""
    return CLEAN_PATTERN.sub('', text).lower()

def get_tokens(text: str) -> set:
    """Extracts significant tokens/keywords from text."""
    # Using list comprehension inside set constructor is faster
    return {word for word in clean_text(text).split() if word not in STOP_WORDS and len(word) > 2}

@app.post("/analyze", response_model=AnalysisResponse)
async def analyze_resumes(request: AnalysisRequest):
    jd_text = request.job_description
    resumes = request.resumes

    if not jd_text or not resumes:
        return AnalysisResponse(ranked_resumes=[])

    # 1. Prepare texts for TF-IDF
    # We will compute similarity between JD and each Resume

    # Process keywords for explicit matching/missing lists
    jd_tokens = get_tokens(jd_text)

    ranked_resumes = []

    # TF-IDF Vectorization
    # We combine JD and all resumes to build the vocabulary
    documents = [jd_text] + [r.text for r in resumes]

    try:
        tfidf = TfidfVectorizer(stop_words='english')
        tfidf_matrix = tfidf.fit_transform(documents)

        # Calculate cosine similarity using vectorized matrix operations
        # instead of manual loops
        jd_vector = tfidf_matrix[0]
        resume_vectors = tfidf_matrix[1:]

        # This compares the single jd_vector against all resume_vectors at once
        similarities = cosine_similarity(jd_vector, resume_vectors)[0]

        # Pre-calculate list data using list comprehensions for speedup
        # by avoiding iterative attribute lookups
        resume_tokens_list = [get_tokens(resume.text) for resume in resumes]

        for i, resume in enumerate(resumes):
            similarity = similarities[i]

            # Keyword Analysis
            resume_tokens = resume_tokens_list[i]
            matches = list(jd_tokens.intersection(resume_tokens))
            missing = list(jd_tokens.difference(resume_tokens))

            ranked_resumes.append(ResumeData(
                id=resume.id,
                name=resume.name,
                text=resume.text,
                score=round(similarity * 100, 2),
                matches=matches,
                missing=missing
            ))

        # Sort by score descending
        ranked_resumes.sort(key=lambda x: x.score, reverse=True)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return AnalysisResponse(ranked_resumes=ranked_resumes)

@app.post("/upload")
async def upload_files(files: List[UploadFile] = File(...)):
    """
    Endpoint to parse uploaded text and pdf files on the server.
    """
    results = []
    for file in files:
        content = await file.read()
        name = file.filename if file.filename else "unknown"
        text = ""
        try:
            if name.lower().endswith(".pdf"):
                # Parse PDF
                pdf_reader = PyPDF2.PdfReader(io.BytesIO(content))
                for page in pdf_reader.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"
            else:
                # Basic text decoding for txt files
                text = content.decode("utf-8")
            results.append({"name": name, "text": text})
        except Exception as e:
            results.append({"name": name, "text": f"Error decoding file: {str(e)}"})

    return results

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
