## 2024-03-24 - Fast NLP and Vectorized Similarities
**Learning:** In Python processing loops (like `main.py`), NLTK resources (stopwords) and regex patterns (`CLEAN_PATTERN`) initialized at the global (module) level optimize tokenization performance by avoiding repeated intra-function initialization. Additionally, `cosine_similarity` uses vectorized matrix operations (comparing a vector against `tfidf_matrix[1:]` at once) instead of manual loops, significantly speeding up resume similarity scoring. Pre-calculating list data using list comprehensions (e.g., extracting tokens from resume objects) provides a measurable speedup by avoiding iterative attribute lookups.
**Action:** Always pre-compile regexes and cache heavy resources like NLTK stopwords globally. Always use scikit-learn's native vectorized matrix operations over manual iteration when processing similarities, and pre-extract loop iterations into list comprehensions.

## 2024-04-25 - Pre-calculate Maximum ID outside file loop
**Learning:** In `App.tsx`, calculating the maximum resume ID inside the file processing loop caused O(N * M) complexity during bulk file uploads because `resumes.map()` is called for every file.
**Action:** Pre-calculate invariants like the maximum ID outside of file processing loops to reduce complexity to O(N + M) and provide a measurable speedup for bulk operations.
