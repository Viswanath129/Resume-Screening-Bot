## 2025-02-19 - [Global Resource Initialization]
**Learning:** Initializing NLTK resources (stopwords) and compiling regex patterns inside request handlers significantly degrades performance (~2.3x slowdown) due to redundant I/O and compilation.
**Action:** Move expensive initializations (NLTK data loading, regex compilation) to the global scope or application startup event.
