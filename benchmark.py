import time
import timeit

setup_code = """
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
import nltk

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

class ResumeData:
    def __init__(self, id, name, text):
        self.id = id
        self.name = name
        self.text = text

# Mock data
jd_text = "Looking for a python developer with fastapi and react experience." * 10
resumes = [ResumeData(i, f"Name {i}", f"Python developer with fastapi experience {i} " * 10) for i in range(100)]

documents = [jd_text] + [r.text for r in resumes]
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(documents)
jd_vector = tfidf_matrix[0]

def clean_text_old(text: str) -> str:
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text.lower()

def get_tokens_old(text: str) -> set:
    stop_words = set(stopwords.words('english'))
    words = clean_text_old(text).split()
    return {word for word in words if word not in stop_words and len(word) > 2}

CLEAN_PATTERN = re.compile(r'[^a-zA-Z\s]')
STOP_WORDS = set(stopwords.words('english'))

def clean_text_new(text: str) -> str:
    text = CLEAN_PATTERN.sub('', text)
    return text.lower()

def get_tokens_new(text: str) -> set:
    words = clean_text_new(text).split()
    return {word for word in words if word not in STOP_WORDS and len(word) > 2}
"""

test_old = """
jd_tokens = get_tokens_old(jd_text)
ranked_resumes = []
for i, resume in enumerate(resumes):
    resume_vector = tfidf_matrix[i + 1]
    similarity = cosine_similarity(jd_vector, resume_vector)[0][0]
    resume_tokens = get_tokens_old(resume.text)
    matches = list(jd_tokens.intersection(resume_tokens))
    missing = list(jd_tokens.difference(resume_tokens))
"""

test_new = """
jd_tokens = get_tokens_new(jd_text)
ranked_resumes = []
similarities = cosine_similarity(jd_vector, tfidf_matrix[1:])[0]
resume_tokens_list = [get_tokens_new(r.text) for r in resumes]

for i, resume in enumerate(resumes):
    similarity = similarities[i]
    resume_tokens = resume_tokens_list[i]
    matches = list(jd_tokens.intersection(resume_tokens))
    missing = list(jd_tokens.difference(resume_tokens))
"""

if __name__ == "__main__":
    t_old = timeit.timeit(test_old, setup=setup_code, number=10)
    t_new = timeit.timeit(test_new, setup=setup_code, number=10)
    print(f"Old: {t_old:.4f}s")
    print(f"New: {t_new:.4f}s")
    print(f"Speedup: {t_old / t_new:.2f}x")
