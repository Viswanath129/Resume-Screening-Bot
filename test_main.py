
import unittest
from main import get_tokens, clean_text

class TestMain(unittest.TestCase):

    def test_clean_text(self):
        text = "Hello, World! 123"
        cleaned = clean_text(text)
        self.assertEqual(cleaned, "hello world ")

    def test_get_tokens(self):
        text = "This is a simple test. Python is great for data science."
        tokens = get_tokens(text)
        expected_tokens = {"simple", "test", "python", "great", "data", "science"}
        self.assertEqual(tokens, expected_tokens)

    def test_get_tokens_stopwords(self):
        text = "the and or of a an"
        tokens = get_tokens(text)
        self.assertEqual(tokens, set())

    def test_get_tokens_short_words(self):
        text = "hi no go"
        tokens = get_tokens(text)
        self.assertEqual(tokens, set())

if __name__ == '__main__':
    unittest.main()
