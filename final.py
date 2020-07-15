import wikipedia
from collections import Counter
import re

topXwords = 250

def GetWordsFrequency(page_title):
    page = wikipedia.page(page_title)

    page = page.content.lower()

    page = re.sub('[^a-z0-9 ]', '', page)

    words = page.split()

    counts = Counter(words)

    unwanted_words = ["the", "in", "of", "and", "to", "a", "on",
                      "for", "was", "as", "from", "with", "by", "that", "at",
                      "an", "after", "which", "not", "be", "had", "is", "it",
                      "also", "during", "who", "were", "their", "where", "his",
                      "about", "he", "she", "her", "them", "its", "they", "has",
                      "are", "have", "most"
                      ]

    for word in unwanted_words:
        if word in counts:
            del counts[word]

    # for item, freq in counts.most_common(topXwords):
    #     print(item, '=', freq )

    total = sum([freq for (word, freq) in counts.most_common(topXwords)])

    return {word : freq / total for (word, freq) in counts.most_common(topXwords)}

def Compare(A, B):
    A_freq = GetWordsFrequency(A)
    B_freq = GetWordsFrequency(B)

    comparedWords = { x : A_freq[x] * (
            1 -
             abs((B_freq[x]-A_freq[x])/A_freq[x])
             ) for x in A_freq if x in B_freq}
    #note that this is an imperfect method for calculating the similarity between two frequency tables. A more suitable method would be a chi-squared test or something.

    score = sum(comparedWords.values())

    print("The similarity score between " + A + " and " + B + " is " + str(score))
    print("")
    print("The most common words are:")
    print(Counter(comparedWords).most_common(10))
    print("")

Compare("Barack Obama", "Barack Obama")
Compare("Barack Obama", "Donald Trump")
Compare("Barack Obama", "Cheese")
Compare("Pakistan", "China")
Compare("Pakistan", "India")