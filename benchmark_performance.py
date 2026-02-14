import timeit
import nltk
from main import get_tokens, clean_text

# Ensure NLTK data is downloaded for the benchmark to run smoothly
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

def benchmark():
    text = "This is a sample resume text with some skills like Python, Java, and C++." * 10

    # Run get_tokens 2000 times
    start_time = timeit.default_timer()
    for _ in range(2000):
        get_tokens(text)
    end_time = timeit.default_timer()

    print(f"Time taken for 2000 calls: {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    benchmark()
