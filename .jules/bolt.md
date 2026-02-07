## 2024-05-22 - [NLTK Stopwords Optimization]
**Learning:** Initializing NLTK resources (like `stopwords.words('english')`) inside a function called per-request is a significant performance bottleneck. It involves disk I/O and set construction on every call.
**Action:** Move such resource loading to the module level (global scope) so it happens only once at startup. Similarly, compile regex patterns globally. Measured impact: ~2.2x speedup on tokenization logic.
