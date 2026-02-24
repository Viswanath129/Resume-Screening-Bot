## 2025-02-23 - Global NLTK Stopwords
**Learning:** Initializing 'stopwords.words("english")' inside a function called in a loop creates significant overhead (approx 30-40% slower).
**Action:** Always move static data loading and regex compilation to the global scope for text processing functions.
