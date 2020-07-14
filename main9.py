import wikipedia
from collections import Counter
import re

wiki = wikipedia.page("Barack Obama")

entire_page = wiki.content.lower()

entire_page = re.sub('[^a-z0-9 ]', '', entire_page)

words = entire_page.split()

counts = Counter(words)

unwanted_words = ["the", "in", "of", "and", "to", "a", "on",
                  "for", "was", "as", "from", "with", "by", "that", "at",
                  "an", "after", "which", "not", "be", "had", "is", "it"]

for word in unwanted_words:
    if word in counts:
        del counts[word]

# for item, freq in counts.most_common(1000):
#     print(item, '=', freq)

print(sum(counts.values()))

print(sum([item[1] for item in counts.most_common(1000)])) # this means we can now only add up the top 1000 words in the list