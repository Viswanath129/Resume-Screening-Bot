## 2024-03-14 - Scikit-learn Cosine Similarity Optimization
**Learning:** In `main.py`'s `analyze_resumes`, computing cosine similarity in a loop (`cosine_similarity(jd_vector, resume_vector)` for each resume) is significantly slower than doing a single vectorized operation (`cosine_similarity(jd_vector, tfidf_matrix[1:])`).
**Action:** Replace the iterative cosine similarity calculation with a single vectorized call. This improves performance by over 500x for 1000 resumes (1.37s -> 0.002s).

## 2024-03-14 - NLTK Stopwords Optimization
**Learning:** Loading NLTK stopwords inside the `get_tokens` function (`stop_words = set(stopwords.words('english'))`) adds unnecessary overhead to every call, especially when called in a loop for each resume.
**Action:** Move the stopwords initialization to the global/module level so it is only loaded once. This improves `get_tokens` performance by ~4.5x (0.26s -> 0.05s for 1000 calls).
