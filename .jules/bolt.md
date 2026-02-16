## 2026-02-16 - Global Stopwords and Regex Initialization

**Learning:** Re-initializing NLTK stopwords set and compiling regex inside a frequently called function (`get_tokens`) caused ~38% performance overhead.
**Action:** Always move static resource initialization (stopwords, regex) to global scope or lazy-load them to avoid re-initialization in loops.
