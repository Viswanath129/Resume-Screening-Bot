## 2026-02-14 - [NLTK Stopwords Loading]
**Learning:** Loading NLTK stopwords inside a loop or frequent function call is extremely slow (file I/O + set creation). Moving it to global scope yielded a 4x speedup.
**Action:** Always load static NLP resources (stopwords, models) at module level.
