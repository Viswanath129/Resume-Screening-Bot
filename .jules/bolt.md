## 2025-03-16 - [Optimize Stopwords and Regex Loading]
**Learning:** Initializing NLTK stopwords and compiling regex patterns inside functions causes significant performance degradation when called repeatedly (e.g., per word/token or per resume). Benchmarking showed a 33x speedup by moving these initializations to the global (module) scope.
**Action:** Always declare heavy resources like NLTK models/stopwords and compile regular expressions at the module level so they are initialized only once.

## 2025-03-16 - [Vectorized Matrix Operations for Cosine Similarity]
**Learning:** Looping over scikit-learn's `tfidf_matrix` to compute cosine similarities one-by-one (`cosine_similarity(vec1, vec2)`) is extremely slow. Scikit-learn is optimized for vectorized matrix operations. By comparing a single vector against a matrix of vectors simultaneously (`cosine_similarity(vec1, matrix[1:])`), the computation for 1000 resumes sped up by over 700x.
**Action:** Never use for-loops for operations that can be vectorized across matrices or arrays using scikit-learn or numpy.
