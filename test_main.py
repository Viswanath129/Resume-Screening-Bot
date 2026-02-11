import unittest
from main import clean_text, get_tokens
import nltk

class TestResumeAnalysis(unittest.TestCase):
    def test_clean_text(self):
        text = "Hello, World! 123"
        cleaned = clean_text(text)
        self.assertEqual(cleaned, "hello world ")

    def test_get_tokens(self):
        text = "This is a simple test case for the resume screening bot."
        tokens = get_tokens(text)
        # stopwords: this, is, a, for, the
        # short words: (none that aren't stopwords here)
        expected = {'simple', 'test', 'case', 'resume', 'screening', 'bot'}
        self.assertEqual(tokens, expected)

if __name__ == '__main__':
    nltk.download('stopwords')
    unittest.main()
