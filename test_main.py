import unittest
from main import clean_text, get_tokens
import nltk

class TestResumeBot(unittest.TestCase):
    def test_clean_text(self):
        text = "Hello, World! 123"
        cleaned = clean_text(text)
        self.assertEqual(cleaned, "hello world ")

    def test_get_tokens(self):
        text = "This is a sample resume with Python and SQL skills."
        tokens = get_tokens(text)
        expected_tokens = {'sample', 'resume', 'python', 'sql', 'skills'}
        # Note: stopwords like 'this', 'is', 'a', 'with', 'and' should be removed
        # Also words <= 2 chars might be filtered depending on implementation
        # Let's check existing logic: len(word) > 2
        self.assertTrue('python' in tokens)
        self.assertTrue('sql' in tokens)
        self.assertFalse('is' in tokens)
        self.assertFalse('a' in tokens)

if __name__ == '__main__':
    unittest.main()
