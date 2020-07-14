# nows the fun bit, lets prepare to compare this list with another pages' list. But first, we'll need to refactor our code so we can re-use it for the other page easily.

import wikipedia
from collections import Counter


def GetWordsFrequency(page_title, topXwords):
    wiki = wikipedia.page(page_title)

    entire_page = wiki.content

    entire_page_lower = entire_page.lower()

    entire_page_lower_filtered = entire_page_lower

    unwanted_signs = [';', ':', '!', "*", "=", ",", ".", "'s", "(", ")"]

    for i in unwanted_signs:
        entire_page_lower_filtered = entire_page_lower_filtered.replace(i, '')

    words = entire_page_lower_filtered.split()

    counts = Counter(words)

    unwanted_words = ["the", "in", "of", "and", "to", "a", "on",
                      "for", "was", "as", "from", "with", "by", "that", "at",
                      "an", "after", "which", "not", "be", "had", "is", "it"]

    for word in unwanted_words:
        if word in counts:
            del counts[word]

    total = sum([item[1] for item in counts.most_common(topXwords)])

    # for item, freq in counts.most_common(topXwords):
    #     print(item, '=', freq/total)

    return [(item, freq / total) for (item, freq) in counts.most_common(topXwords)]


print(GetWordsFrequency("Barack Obama", 10))
print(GetWordsFrequency("Donald Trump", 10))

# alright, now we want to compare the two lists and come up with a single number that gives us a score of how similar they two are
# my approach is going to be to go through each word in the obama list, find that same word in the trump list, and multiply the score together
# and add them up