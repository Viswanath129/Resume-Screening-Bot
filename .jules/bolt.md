## 2025-05-18 - [Re-initialization of NLTK Resources]
**Learning:** Re-initializing `stopwords.words('english')` inside a frequently called function is a significant performance bottleneck because it loads and processes the corpus every time.
**Action:** Move static resource initializations (like NLTK stop words and regex compilations) to the module level (global scope) or use memoization.
