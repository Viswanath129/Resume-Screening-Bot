## 2026-02-02 - [NLTK Resource Loading Overhead]
**Learning:** Loading NLTK resources like `stopwords.words('english')` involves significant I/O and object creation overhead (~150ms+ in loops). Doing this inside a request handler (or worse, inside a loop over items in a request) kills performance.
**Action:** Always initialize NLTK corpora and other heavy resources (like Regex compilation) at the module level (global scope) so they are loaded only once at startup.
