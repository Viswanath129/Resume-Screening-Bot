import unittest
from main import clean_text, get_tokens

class TestTokenization(unittest.TestCase):
    def test_clean_text(self):
        self.assertEqual(clean_text("Hello, World!"), "hello world")
        self.assertEqual(clean_text("Python 3.9"), "python ")
        self.assertEqual(clean_text("UPPERcase"), "uppercase")
        self.assertEqual(clean_text("  spaces  "), "  spaces  ")

    def test_get_tokens(self):
        text = "This is a sample text with some stopwords and keywords."
        tokens = get_tokens(text)
        expected_tokens = {'sample', 'text', 'stopwords', 'keywords'}
        self.assertEqual(tokens, expected_tokens)

        text2 = "Python is great for data science."
        tokens2 = get_tokens(text2)
        expected_tokens2 = {'python', 'great', 'data', 'science'}
        self.assertEqual(tokens2, expected_tokens2)

if __name__ == '__main__':
    unittest.main()
