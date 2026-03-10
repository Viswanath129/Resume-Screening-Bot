## 2024-03-10 - Vectorized operations in scikit-learn
**Learning:** In scikit-learn, using vectorized matrix operations for cosine_similarity (e.g., comparing a single vector against a matrix like `tfidf_matrix[1:]` at once) is significantly faster than looping over individual vectors to compute similarity.
**Action:** Always prefer matrix/vector operations over loops in scikit-learn.
