## 2024-03-07 - [Optimization of `get_tokens` and `cosine_similarity`]
**Learning:**
- Instantiating `stopwords.words('english')` (NLTK) and compiling regexes inside a function called frequently (like `get_tokens`, which is called for each resume) introduces significant overhead.
- `cosine_similarity` in `scikit-learn` is highly optimized for vector operations. Comparing a 1D vector to a 2D matrix (like `tfidf_matrix[1:]`) all at once is substantially faster than iterating over each row and comparing them one by one.

**Action:**
- Always cache shared resources (like regex objects and stopwords) at the module level.
- When performing similarity calculations on multiple items, vectorize the operation across the entire matrix rather than looping through individual vectors.
