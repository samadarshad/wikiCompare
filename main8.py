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

for item, freq in counts.most_common(1000):
    print(item, '=', freq)

# alright, I think we're ready to use this data.
# now, we want to compare this page with other pages. The way we'll do this is to compare the relative frequency of the words
# lets get to calculating the relative frequency for each word
