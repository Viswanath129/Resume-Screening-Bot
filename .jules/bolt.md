## 2024-05-24 - NLTK Stopwords and Regex Initialization
**Learning:** Re-initializing `set(stopwords.words('english'))` and `re.compile` inside a frequently called function (`get_tokens` and `clean_text`) causes significant overhead (overhead of file I/O or processing per call). Moving these to global scope resulted in a ~15x speedup for the tokenization process.
**Action:** Always verify if resource-heavy initializations (like loading corpora or compiling regex) are happening inside loops or frequently called functions. Move them to module level or use lazy initialization/caching.
