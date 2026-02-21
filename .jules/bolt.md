## 2024-10-26 - [Python Stopwords Optimization]
**Learning:** Loading NLTK stopwords inside a frequently called function is a massive performance bottleneck. In this case, `get_tokens` was called for every resume, re-loading the stopwords list from disk/memory each time. Moving it to global scope reduced execution time by ~96% (0.132s -> 0.005s per 1000 calls).
**Action:** Always initialize heavy resources like NLTK corpora or regex patterns at the module level, not inside hot loops or request handlers.
