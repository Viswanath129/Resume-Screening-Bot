import unittest
from main import get_tokens, clean_text

class TestResumeAnalysis(unittest.TestCase):
    def test_clean_text(self):
        self.assertEqual(clean_text("Hello World! 123"), "hello world ")
        self.assertEqual(clean_text("Python & Java"), "python  java")

    def test_get_tokens(self):
        text = "The quick brown fox jumps over the lazy dog."
        tokens = get_tokens(text)
        # stopwords: the, over
        # short words: fox, dog (wait, len > 2, so fox (3) is kept, dog (3) is kept)
        # "fox" len is 3. > 2 is True.
        expected = {'quick', 'brown', 'fox', 'jumps', 'lazy', 'dog'}
        # "the" is stopword. "over" is stopword.
        self.assertEqual(tokens, expected)

    def test_get_tokens_stopwords(self):
        text = "and or but if then"
        tokens = get_tokens(text)
        self.assertEqual(tokens, set()) # All should be removed or too short (if, or)

if __name__ == '__main__':
    unittest.main()
