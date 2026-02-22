import re
from collections import Counter

STOPWORDS = {"the", "and", "is", "of", "to", "in", "a", "for", "on", "with"}


def analyze_words(titles):
    combined_text = " ".join(titles).lower()
    combined_text = re.sub(r'[^\w\s]', '', combined_text)

    words = combined_text.split()
    words = [w for w in words if w not in STOPWORDS]

    counter = Counter(words)

    repeated = {word: count for word, count in counter.items() if count >= 2}

    return repeated