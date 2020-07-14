import wikipedia
from collections import Counter

wiki = wikipedia.page("Barack Obama")

entire_page = wiki.content

words = entire_page.lower().split() # here we can now see that president = 57

counts = Counter(words)

for item, freq in counts.most_common(1000):
    print(item, '=', freq)