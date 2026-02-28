## 2025-02-28 - [Stopwords and Regex Initialization Bottleneck in Fast API]
**Learning:** Initializing expensive objects like `set(stopwords.words('english'))` and compiling regex patterns via `re.sub(r'[^a-zA-Z\s]', '', text)` inside frequently called helper functions like `get_tokens` and `clean_text` causes a massive performance overhead per request.
**Action:** Always move heavy initializations like NLTK stopwords set loading and regex compilation to the module level so they are initialized exactly once upon application startup instead of on every request.
