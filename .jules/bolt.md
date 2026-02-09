## 2026-02-09 - NLTK Performance Pitfall
**Learning:** Loading NLTK resources like `stopwords.words()` inside a function call adds significant overhead due to repeated file I/O and set construction.
**Action:** Initialize NLTK resources and compile regex patterns at the global/module level to ensure they are loaded only once.
