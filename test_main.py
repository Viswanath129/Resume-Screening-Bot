import unittest
from main import clean_text, get_tokens

class TestTextProcessing(unittest.TestCase):
    def test_clean_text(self):
        input_text = "Hello, World! 123"
        expected = "hello world "
        self.assertEqual(clean_text(input_text), expected)

    def test_get_tokens(self):
        input_text = "The quick brown fox jumps over the lazy dog."
        tokens = get_tokens(input_text)
        # stopwords: 'the', 'over'
        # short words: none here except 'fox', 'dog' are > 2
        # 'the' is removed.
        # 'quick', 'brown', 'fox', 'jumps', 'lazy', 'dog' should be present.
        expected_tokens = {'quick', 'brown', 'fox', 'jumps', 'lazy', 'dog'}
        self.assertEqual(tokens, expected_tokens)

    def test_get_tokens_stopwords(self):
        input_text = "This is a test of the stopwords removal."
        tokens = get_tokens(input_text)
        # 'this', 'is', 'a', 'of', 'the' are stopwords.
        # 'test', 'stopwords', 'removal' should remain.
        expected_tokens = {'test', 'stopwords', 'removal'}
        self.assertEqual(tokens, expected_tokens)

    def test_get_tokens_short_words(self):
        input_text = "go to it"
        tokens = get_tokens(input_text)
        # 'go', 'to', 'it' are all length 2.
        self.assertEqual(tokens, set())

if __name__ == '__main__':
    unittest.main()
