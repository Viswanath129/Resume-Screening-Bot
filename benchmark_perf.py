import timeit
import re
from nltk.corpus import stopwords
import main

# Sample text
text = "Experienced Python developer with a background in Flask and Django. Familiar with SQL and basic ML concepts." * 100

# Original implementation (recreated for comparison)
def clean_text_orig(text: str) -> str:
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text.lower()

def get_tokens_orig(text: str) -> set:
    stop_words = set(stopwords.words('english'))
    words = clean_text_orig(text).split()
    return {word for word in words if word not in stop_words and len(word) > 2}

# Run benchmarks
def run_benchmark():
    iterations = 1000

    time_orig = timeit.timeit(lambda: get_tokens_orig(text), number=iterations)
    time_opt = timeit.timeit(lambda: main.get_tokens(text), number=iterations)

    print(f"Original: {time_orig:.4f}s")
    print(f"Optimized (main.py): {time_opt:.4f}s")
    print(f"Improvement: {(time_orig - time_opt) / time_orig * 100:.2f}%")

if __name__ == "__main__":
    run_benchmark()
