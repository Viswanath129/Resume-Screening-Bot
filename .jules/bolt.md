## 2025-03-02 - Initialization\n**Learning:** Creating journal to store critical learnings.\n**Action:** Use journal to keep track of bottlenecks and specific codebase patterns.

## 2025-03-02 - Backend Stop Words & Regex Performance
**Learning:** Found a performance bottleneck where NLTK stop words and `re.compile()` were being executed inside the `get_tokens()` and `clean_text()` functions on every single text segment. Since these values are static, fetching/compiling them inside the loop resulted in significant unnecessary overhead.
**Action:** When working with static sets like stop words or complex regex patterns in loops/frequent function calls, always move them to the global scope or initialize them once to save execution time.
