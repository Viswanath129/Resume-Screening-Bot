## 2024-03-24 - Fast NLP and Vectorized Similarities
**Learning:** In Python processing loops (like `main.py`), NLTK resources (stopwords) and regex patterns (`CLEAN_PATTERN`) initialized at the global (module) level optimize tokenization performance by avoiding repeated intra-function initialization. Additionally, `cosine_similarity` uses vectorized matrix operations (comparing a vector against `tfidf_matrix[1:]` at once) instead of manual loops, significantly speeding up resume similarity scoring. Pre-calculating list data using list comprehensions (e.g., extracting tokens from resume objects) provides a measurable speedup by avoiding iterative attribute lookups.
**Action:** Always pre-compile regexes and cache heavy resources like NLTK stopwords globally. Always use scikit-learn's native vectorized matrix operations over manual iteration when processing similarities, and pre-extract loop iterations into list comprehensions.

## 2024-05-30 - Concurrent Upload I/O
**Learning:** Sequential `await` calls in loops (like `await file.read()` for multiple uploads) block the event loop and prevent I/O operations from running concurrently.
**Action:** Use `asyncio.gather(*[coroutine(item) for item in items])` to execute independent I/O tasks (like file reads) concurrently, significantly reducing total processing time.
