## 2024-05-23 - Python NLTK Stopwords Optimization
**Learning:** Initializing `set(stopwords.words('english'))` inside a frequently called function (`get_tokens`) caused massive overhead due to repeated set construction and list lookup. Moving it to global scope yielded a ~24x speedup (1.34s -> 0.05s for 10k iterations).
**Action:** Always verify if heavy initializations (like NLTK resources or Regex compilation) happen inside loops or hot paths. Lift them to module level or use caching.
