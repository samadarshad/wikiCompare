# nows the fun bit, lets prepare to compare this list with another pages' list. But first, we'll need to refactor our code so we can re-use it for the other page easily.

import wikipedia
from collections import Counter

pageA = "Barack Obama"
pageB = "Donald Trump"
topXwords = 10

def GetWordsFrequency(page_title):
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

    return {item : freq / total for (item, freq) in counts.most_common(topXwords)}


pageA_dictionary = GetWordsFrequency("Barack Obama")
pageB_dictionary = GetWordsFrequency("Donald Trump")

print(pageA_dictionary)
print(pageB_dictionary)

shared_items = {x: pageA_dictionary[x]*pageB_dictionary[x] for x in pageA_dictionary if x in pageB_dictionary}
print(shared_items)


vals = [pageA_dictionary[x]*pageB_dictionary[x] for x in pageA_dictionary if x in pageB_dictionary]
print(vals)
print("The similarity score between " + pageA + " and " + pageB + " is " + str(sum(vals)))

