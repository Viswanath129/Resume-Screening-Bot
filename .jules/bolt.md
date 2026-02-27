# Bolt's Journal ⚡

## 2025-02-20 - [Text Processing Bottleneck]
**Learning:** Loading NLTK stopwords and compiling regex inside a function called in a loop (like `get_tokens`) is a significant performance bottleneck.
**Action:** Always move static resource loading (stopwords, heavy models) and regex compilation to the global scope or a class initializer.
