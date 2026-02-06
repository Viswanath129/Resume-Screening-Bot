## 2025-02-23 - Global NLTK Resource Initialization
**Learning:** Initializing NLTK resources (like `stopwords`) inside a function adds significant overhead (IO/set creation) per call. However, when moving them to global scope, one must ensure `nltk.download` happens *before* the global variable assignment to avoid `LookupError` during module import.
**Action:** Always check resource availability (download if needed) before defining global constants that depend on them, or use lazy initialization patterns.
