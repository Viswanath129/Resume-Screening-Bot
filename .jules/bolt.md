## 2025-02-18 - NLTK Stopwords Overhead
**Learning:** Loading NLTK stopwords inside request handlers (`set(stopwords.words('english'))`) adds ~150ms latency per batch of calls (14% overhead). NLTK reads from disk each time.
**Action:** Always move static resource loading (stopwords, models, regex compilation) to global scope or lazy-loaded module-level singletons in FastAPI apps.
