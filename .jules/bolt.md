## 2026-02-13 - [NLTK Stopwords Loading Bottleneck]
**Learning:** Loading NLTK stopwords inside a function called in a loop creates significant overhead (file I/O and object creation).
**Action:** Always load static resources like stopwords and compile regex patterns at the module level (global scope) in Python backend services.
