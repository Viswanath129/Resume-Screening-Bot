## 2026-03-01 - Optimize NLTK Stopwords and Regex Compilation
**Learning:** Initializing regular expressions (`re.compile`) and heavy resources like NLTK's stopwords set inside frequently called functions (like `get_tokens`) creates a significant performance bottleneck due to redundant loading/compilation on every call.
**Action:** Always move static resources and regex compilations to the global (module) scope so they are only initialized once at startup.
