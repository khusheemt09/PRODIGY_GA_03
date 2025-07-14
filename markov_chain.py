import random
import re

#  Read text with punctuation
with open("input.txt", "r", encoding="utf-8") as f:
    text = f.read()

#  Keep punctuation at the end of words
words = re.findall(r"\b\w+(?:[.!?])?", text.lower())

#  Build trigram model
markov_chain = {}
for i in range(len(words) - 3):
    key = (words[i], words[i+1], words[i+2])
    next_word = words[i+3]
    markov_chain.setdefault(key, []).append(next_word)

#  Generate sentence that ends on full stop
def generate_text(chain, start_words, max_length=50):
    if start_words not in chain:
        print(f"⚠️ Start words {start_words} not found.")
        return ""

    w1, w2, w3 = start_words
    result = [w1, w2, w3]

    for _ in range(max_length):
        next_options = chain.get((w1, w2, w3), [])
        if not next_options:
            break
        next_word = random.choice(next_options)
        result.append(next_word)

        if next_word.endswith((".", "!", "?")):
            break

        w1, w2, w3 = w2, w3, next_word

    return ' '.join(result).capitalize()

#  Ask user for start words
start_input = input("🟢 Enter 3 start words : ").strip().lower().split()

if len(start_input) == 3:
    start_tuple = tuple(start_input)
    output = generate_text(markov_chain, start_tuple)
    print("\n📝 Generated Text:\n")
    print(output)
else:
    print("⚠️ Please enter exactly three words.")
