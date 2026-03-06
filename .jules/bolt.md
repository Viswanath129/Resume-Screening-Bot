## 2024-05-19 - [Vectorized Cosine Similarity in Scikit-learn]
**Learning:** Using `cosine_similarity(jd_vector, tfidf_matrix[1:])` is significantly faster than looping over `tfidf_matrix` and calling `cosine_similarity(jd_vector, resume_vector)` one by one in Python.
**Action:** When comparing a single vector against many vectors using scikit-learn or numpy, always use matrix operations to compare against the entire block of vectors at once instead of using Python `for` loops.
