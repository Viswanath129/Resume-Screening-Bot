## 2024-05-22 - Globalizing NLTK Resources
**Learning:** Initializing NLTK resources (like `stopwords.words()`) and compiling regexes inside a frequently called function (like `get_tokens`) creates a significant performance bottleneck due to repeated I/O and processing.
**Action:** Always move static resource initialization and regex compilation to the global scope or application startup to ensure they are computed only once.
