
## $(date +%Y-%m-%d) - [Vectorized Matrix Similarity in scikit-learn]
**Learning:** Computing cosine similarity inside a Python loop (e.g. `for i in range(len(resumes))`) is a massive bottleneck. Passing a multi-row matrix (`resume_vectors`) against a single-row matrix (`jd_vector`) to `cosine_similarity` pushes the calculation down to optimized C/NumPy level and speeds up processing time dramatically. Additionally, re-initializing NLTK `stopwords` (a set construction + file lookup) during text tokenization adds significant unnecessary overhead on repeated calls.
**Action:** When working with scikit-learn or similar data science libraries, look for opportunities to replace `for` loops with vectorized matrix array operations, and cache NLTK lookups globally at the module level.
