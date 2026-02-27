
import unittest
from main import clean_text, get_tokens, CLEAN_TEXT_REGEX, STOP_WORDS
import re

class TestTextProcessing(unittest.TestCase):
    def test_clean_text(self):
        self.assertEqual(clean_text("Hello, World!"), "hello world")
        self.assertEqual(clean_text("Python 3.12"), "python ")
        self.assertEqual(clean_text(""), "")

    def test_get_tokens(self):
        text = "This is a sample sentence with Python and Machine Learning."
        tokens = get_tokens(text)
        expected = {'sample', 'sentence', 'python', 'machine', 'learning'}
        self.assertEqual(tokens, expected)

    def test_constants_optimization(self):
        # Verify that constants are used
        self.assertIsInstance(CLEAN_TEXT_REGEX, re.Pattern)
        self.assertIsInstance(STOP_WORDS, set)
        self.assertTrue(len(STOP_WORDS) > 0)

if __name__ == "__main__":
    unittest.main()
