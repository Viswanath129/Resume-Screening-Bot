## 2024-05-24 - [NLTK Stopwords Optimization]
**Learning:** Loading NLTK stopwords inside a frequently called function (like `get_tokens`) is a significant performance bottleneck. Also, recompiling regex patterns every time is slow.
**Action:** Move stopwords loading and regex compilation to the global scope to reduce execution time.
