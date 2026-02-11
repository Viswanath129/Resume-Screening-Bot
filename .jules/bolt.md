## 2025-02-18 - Optimize Text Processing Initialization
**Learning:** Loading NLTK stopwords and compiling regexes inside a function that is called repeatedly (like in a loop) is a significant performance bottleneck. In `get_tokens`, `stopwords.words('english')` was being re-loaded from disk/memory and converted to a set on every call, and `re.sub` was re-compiling the pattern.
**Action:** Move static resource initialization (stopwords, regex patterns) to the global scope or module level so they are computed only once. This resulted in a ~3x speedup for the `get_tokens` function.
