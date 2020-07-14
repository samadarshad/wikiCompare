import wikipedia
from collections import Counter

wiki = wikipedia.page("Barack Obama")

entire_page = wiki.content

entire_page_lower = entire_page.lower()

entire_page_lower_filtered = entire_page_lower

unwanted_words = [';', ':', '!', "*", "=", ",", ".",
                  "the", "in", "of", "and", "to", "a", "on",
                  "for", "was", "as", "from", "with", "by", "that", "at",
                  "an", "after", "which", "not", "be", "had", "is", "it"]
for i in unwanted_words :
    entire_page_lower_filtered = entire_page_lower_filtered.replace(i, '')

words = entire_page_lower_filtered.split()

counts = Counter(words)

for item, freq in counts.most_common(1000):
    print(item, '=', freq)

# here we can see, we've done something unexpected, we've got rid of those particles, but its also messed with the origional data too
# so lets take a different approach to filtering our data
# instead, lets keep to this approach for the commas and equal signs, but for the removal of words, lets remove them directly from the sorted list rather than from the page