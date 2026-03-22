## 2024-05-15 - [Backend Performance Pattern: Regex & Stopwords Initialization]
**Learning:** In Python processing loops (like `main.py`), initializing NLTK resources (stopwords) and regex patterns (`CLEAN_PATTERN`) at the global (module) level prevents repeated intra-function initialization, providing significant tokenization performance improvements.
**Action:** Always pre-compile regexes and set structures at the global level before using them inside heavily called functions or loops.

## 2024-05-15 - [Backend Performance Pattern: Vectorized Operations vs Manual Loops]
**Learning:** In `main.py`, calculating cosine similarity inside a loop (`cosine_similarity(jd_vector, resume_vector)`) is inefficient. Using vectorized matrix operations (`cosine_similarity(jd_vector, tfidf_matrix[1:])`) to compare a vector against all other vectors at once avoids manual loops and significantly speeds up similarity scoring. Additionally, pre-calculating list data using list comprehensions (e.g., extracting tokens from resume objects) provides a measurable speedup over iterative attribute lookups.
**Action:** When computing similarities or processing lists of data, prefer vectorized NumPy/Scikit-learn operations and list comprehensions over standard Python loops.
