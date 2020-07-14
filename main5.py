import wikipedia
from collections import Counter

wiki = wikipedia.page("Barack Obama")

entire_page = wiki.content

words = entire_page.split()

counts = Counter(words)
# print(counts)


# use the below for a more friendly way to view
for item, freq in counts.most_common(1000):
    print(item, '=', freq)

# now, we can inspect our table and see that we want to get rid of some stuff,
# these particles "the, and, because, in, a, on" etc
# some of these commas, equal signs, fullstops
# and we dont want to make a distinction between capital and noncapital letters i.e. President = 33, president = 24. we dont want that distinction
# so lets fix that