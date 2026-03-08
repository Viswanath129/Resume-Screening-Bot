
## 2024-05-19 - Vectorizing Cosine Similarity
**Learning:** `cosine_similarity` in scikit-learn is highly optimized for matrix operations. Looping over vectors to compute cosine similarity against a single vector is extremely slow compared to passing the entire matrix slice `tfidf_matrix[1:]` and calculating similarity in one vectorized call.
**Action:** Always compute cosine similarity for an entire batch or matrix when comparing one-to-many items in scikit-learn, instead of using Python loops.
