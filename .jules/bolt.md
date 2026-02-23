## 2026-02-23 - Python NLTK Stopwords Overhead
**Learning:** Loading NLTK stopwords inside a frequently called function (`get_tokens`) caused significant overhead (~58% slowdown).
**Action:** Always move static resource loading (stopwords, heavy models) and regex compilation to module-level constants to ensure O(1) per-call cost instead of O(N).
