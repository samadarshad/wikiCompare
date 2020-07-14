import wikipedia
from collections import Counter

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

def Compare(A, B):
    pageA_dictionary = GetWordsFrequency(A)
    pageB_dictionary = GetWordsFrequency(B)

    vals = [pageA_dictionary[x]*pageB_dictionary[x] for x in pageA_dictionary if x in pageB_dictionary]

    print("The similarity score between " + A + " and " + B + " is " + str(sum(vals)))

Compare("Barack Obama", "Cheese")
Compare("Barack Obama", "Donald Trump")
Compare("Barack Obama", "Hillary Clinton")

#The similarity score between Barack Obama and Cheese is          0.0027870668459589612
#The similarity score between Barack Obama and Donald Trump is    0.026775065006901966
#The similarity score between Barack Obama and Hillary Clinton is 0.011049359566174189
