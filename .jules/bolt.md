## 2024-05-24 - Vectorized Cosine Similarity
**Learning:** In scikit-learn, calling `cosine_similarity` in a loop for individual vectors is a significant anti-pattern. `cosine_similarity` has a lot of overhead for input validation and conversion on each call.
**Action:** Always use vectorized matrix operations when comparing one vector against many (e.g., `cosine_similarity(X, Y)` where Y is a matrix of all documents) rather than looping.
