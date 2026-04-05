import os
import re
from typing import List, Optional
from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
from nltk.corpus import stopwords
import uvicorn

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
        # using a fast sparse matrix dot product instead of cosine_similarity
        similarities = (resume_vectors @ jd_vector.T).toarray().ravel()

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
    Helper endpoint to parse uploaded files on the server if needed.
    For this "make it real" version, we might just read text on client
    and send to /analyze, but this adds flexibility for PDF support later.
    """
    results = []
    for file in files:
        content = await file.read()
        try:
            # Basic text decoding, expand for PDF/Docx later if needed
            text = content.decode("utf-8")
            results.append({"name": file.filename, "text": text})
        except:
            results.append({"name": file.filename, "text": "Error decoding file."})

    return results

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
