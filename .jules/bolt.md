## 2026-02-08 - [NLTK Stopwords Bottleneck]
**Learning:** Loading `nltk.corpus.stopwords.words('english')` inside a frequently called function (`get_tokens`) is a significant performance bottleneck due to repeated file I/O and set construction (O(N) operation per request).
**Action:** Move static resource initialization (like stopwords and regex compilation) to the global scope or application startup to ensure it runs only once (O(1) per request).
