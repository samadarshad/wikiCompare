import wikipedia
from collections import Counter

pageA_name = "Barack Obama"
pageB_name = "Hillary Clinton"
topXwords = 25

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

    return {item : freq / total for (item, freq) in counts.most_common(topXwords)}


pageA_dictionary = GetWordsFrequency(pageA_name)
pageB_dictionary = GetWordsFrequency(pageB_name)

vals = [pageA_dictionary[x] * (1 - (pageB_dictionary[x] - pageA_dictionary[x])) for x in pageA_dictionary if
        x in pageB_dictionary]

print("The similarity score between " + pageA_name + " and " + pageB_name + " is " + str(sum(vals)))


#The similarity score between Barack Obama and Cheese is          0.0027870668459589612
#The similarity score between Barack Obama and Donald Trump is    0.026775065006901966
#The similarity score between Barack Obama and Hillary Clinton is 0.011049359566174189
