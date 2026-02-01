## 2026-02-01 - [NLTK Stopwords Loading in Loop]
**Learning:** Loading NLTK resources (like stopwords) and compiling regex patterns inside a function called in a loop causes significant performance overhead due to repeated I/O and compilation.
**Action:** Always initialize static resources and compile regex patterns at the module level (globally) to ensure they are processed only once at startup.
