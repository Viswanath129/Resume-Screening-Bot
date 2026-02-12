import unittest
from main import clean_text, get_tokens
import nltk

class TestResumeAnalysis(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Ensure NLTK data is available
        try:
            nltk.data.find('corpora/stopwords')
        except LookupError:
            nltk.download('stopwords')

    def test_clean_text(self):
        self.assertEqual(clean_text("Hello, World!"), "hello world")
        self.assertEqual(clean_text("Python 3.12"), "python ") # Digits are removed by the regex [^a-zA-Z\s]
        self.assertEqual(clean_text("  Spaces  "), "  spaces  ")

    def test_get_tokens(self):
        text = "The quick brown fox jumps over the lazy dog."
        tokens = get_tokens(text)
        expected = {'quick', 'brown', 'fox', 'jumps', 'lazy', 'dog'}
        # 'the', 'over' are stopwords. len('dog')=3 > 2.
        self.assertEqual(tokens, expected)

    def test_get_tokens_empty(self):
        self.assertEqual(get_tokens(""), set())

    def test_get_tokens_stopwords_only(self):
        self.assertEqual(get_tokens("the and or but"), set())

if __name__ == '__main__':
    unittest.main()
