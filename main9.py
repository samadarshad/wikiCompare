import wikipedia
from collections import Counter

wiki = wikipedia.page("Barack Obama")

entire_page = wiki.content

entire_page_lower = entire_page.lower()

entire_page_lower_filtered = entire_page_lower

unwanted_signs = [';', ':', '!', "*", "=", ",", ".", "'s", "(", ")"]

for i in unwanted_signs :
    entire_page_lower_filtered = entire_page_lower_filtered.replace(i, '')

words = entire_page_lower_filtered.split()

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