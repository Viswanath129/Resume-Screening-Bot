import unittest
import nltk

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

from main import get_tokens, clean_text

class TestMain(unittest.TestCase):
    def test_clean_text(self):
        text = "Hello, World! 123"
        cleaned = clean_text(text)
        self.assertEqual(cleaned, "hello world ")

        text2 = "Python3.8 is Awesome!"
        cleaned2 = clean_text(text2)
        # Assuming the original regex r'[^a-zA-Z\s]' removes numbers too
        self.assertEqual(cleaned2, "python is awesome")

    def test_get_tokens(self):
        text = "This is a simple test case for stopwords removal."
        tokens = get_tokens(text)
        expected = {"simple", "test", "case", "stopwords", "removal"}
        # 'this', 'is', 'a', 'for' are stopwords.
        # Assuming stopwords are removed and words are lowercased.
        self.assertEqual(tokens, expected)

    def test_get_tokens_short_words(self):
        text = "a ab abc abcd"
        tokens = get_tokens(text)
        # words > 2 chars: abc, abcd
        expected = {"abc", "abcd"}
        self.assertEqual(tokens, expected)

if __name__ == '__main__':
    unittest.main()
