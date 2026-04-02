## 2024-03-24 - Fast NLP and Vectorized Similarities
**Learning:** In Python processing loops (like `main.py`), NLTK resources (stopwords) and regex patterns (`CLEAN_PATTERN`) initialized at the global (module) level optimize tokenization performance by avoiding repeated intra-function initialization. Additionally, `cosine_similarity` uses vectorized matrix operations (comparing a vector against `tfidf_matrix[1:]` at once) instead of manual loops, significantly speeding up resume similarity scoring. Pre-calculating list data using list comprehensions (e.g., extracting tokens from resume objects) provides a measurable speedup by avoiding iterative attribute lookups.
**Action:** Always pre-compile regexes and cache heavy resources like NLTK stopwords globally. Always use scikit-learn's native vectorized matrix operations over manual iteration when processing similarities, and pre-extract loop iterations into list comprehensions.

## 2024-03-24 - Native Set Operations for Filtering
**Learning:** In Python, using native set operations like set difference (`words - STOP_WORDS`) for filtering out stopwords is significantly faster than using comprehensions with inclusion checks (`if word not in STOP_WORDS`) due to execution at the C level.
**Action:** Use native set difference when filtering items from a list of words using a set.
