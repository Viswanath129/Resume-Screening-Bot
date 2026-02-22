## 2026-02-22 - Repeated Resource Initialization in Loops
**Learning:** The `get_tokens` function, which is called for every resume (O(N)), was re-initializing the NLTK stopwords set and re-compiling the regex pattern on every call. This introduced significant overhead (latency) that scaled linearly with the number of resumes.
**Action:** Always inspect functions called inside loops for resource initialization. Move static resources (like large sets, compiled regexes, models) to the global scope or use lazy initialization.
