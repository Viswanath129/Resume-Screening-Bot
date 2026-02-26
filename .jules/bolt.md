## 2026-02-26 - [Stopwords Initialization]
**Learning:** Loading NLTK stopwords inside a function called repeatedly (e.g., `get_tokens`) adds significant overhead (~25%).
**Action:** Initialize static resources like stopwords and regex patterns at the module level.
