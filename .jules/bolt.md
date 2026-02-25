## 2024-02-14 - Python NLTK Bottleneck
**Learning:** Initializing `nltk.corpus.stopwords.words('english')` inside a loop or function called repeatedly (like `get_tokens`) is extremely costly due to file I/O and set conversion. In this codebase, it was causing ~60% overhead per resume analysis.
**Action:** Always move static resource initialization (regex compilation, NLTK corpus loading) to the global scope or a cached function.
