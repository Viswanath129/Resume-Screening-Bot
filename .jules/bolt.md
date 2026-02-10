## 2024-05-23 - [NLTK Resource Initialization]
**Learning:** Initializing NLTK resources (like stopwords) and compiling regex patterns inside request handlers causes significant overhead (file I/O and compilation).
**Action:** Move all static resource loading and compilation to the module level (global scope) to run only once at startup.
