from browserstack_runner import run_parallel_tests
from googletrans import Translator
from collections import Counter
import re
import json

def main():
    results = run_parallel_tests()
    translator = Translator()

    final_results = {}  # Store results with translations and repeated words

    print("\n================ FINAL OUTPUT ================\n")

    for browser_name, articles in results.items():
        print(f"\n===== {browser_name} =====\n")
        final_results[browser_name] = []

        for article in articles:
            # Original text
            title = article["title"]
            content = article["content"]

            # ---- 1. Translate title and content ----
            translated_title = translator.translate(title, src='es', dest='en').text
            translated_content = translator.translate(content, src='es', dest='en').text

            # ---- 2. Find repeated words in translated content ----
            words = re.findall(r'\b\w+\b', translated_content.lower())
            word_counts = Counter(words)
            repeated_words = {word: count for word, count in word_counts.items() if count > 1}

            # ---- 3. Print results ----
            print("Title:", title)
            print("Translated Title:", translated_title)
            print("Content:", content)
            print("Translated Content:", translated_content)
            print("Repeated Words:", repeated_words)
            print("-" * 60)

            # ---- 4. Save to final results for JSON ----
            final_results[browser_name].append({
                "title": title,
                "translated_title": translated_title,
                "content": content,
                "translated_content": translated_content,
                "repeated_words": repeated_words
            })

    # ---- 5. Save everything to JSON ----
    with open("output.json", "w", encoding="utf-8") as f:
        json.dump(final_results, f, ensure_ascii=False, indent=4)

    print("\nSaved results to output.json")

if __name__ == "__main__":
    main()