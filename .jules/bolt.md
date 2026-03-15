## 2024-05-28 - Vectorized matrix operations for scikit-learn
**Learning:** Vectorized matrix operations for `cosine_similarity` in scikit-learn (e.g., comparing a vector against `tfidf_matrix[1:]` at once) is significantly faster than looping over individual vectors, especially for larger arrays.
**Action:** When computing similarities for a batch of documents, always slice the sparse matrix to perform a single batch comparison rather than looping over documents to compare them one by one.
