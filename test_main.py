import unittest
from main import get_tokens, clean_text

class TestMain(unittest.TestCase):
    def test_clean_text(self):
        # clean_text removes non-alpha characters (except space) and lowercases
        self.assertEqual(clean_text("Hello World!"), "hello world")
        # "Python 3.9" -> "python " because numbers are removed
        self.assertEqual(clean_text("Python 3.9"), "python ")
        self.assertEqual(clean_text("Testing... 123"), "testing ")

    def test_get_tokens(self):
        text = "This is a sample text with some stopwords like and, the, of."
        tokens = get_tokens(text)

        # Check stopwords are removed
        self.assertNotIn('the', tokens)
        self.assertNotIn('is', tokens)
        self.assertNotIn('and', tokens)

        # Check significant words are present
        self.assertIn('sample', tokens)
        self.assertIn('text', tokens)

        # Check length filtering (len > 2)
        self.assertNotIn('a', tokens) # len 1
        self.assertNotIn('of', tokens) # len 2

if __name__ == '__main__':
    unittest.main()
