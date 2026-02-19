## 2025-05-23 - [Regex & Stopwords Re-Initialization]
**Learning:** Moving `re.compile` and `stopwords.words()` from function scope to global scope yielded a ~34% performance improvement in tokenization.
**Action:** Always check helper functions called in loops for expensive re-initializations of static resources.
