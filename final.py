import wikipedia
from collections import Counter
import re

topXwords = 25

def GetWordsFrequency(page_title):
    wiki = wikipedia.page(page_title)

    entire_page = wiki.content.lower()

    entire_page = re.sub('[^a-z0-9 ]', '', entire_page)

    words = entire_page.split()

    counts = Counter(words)

    unwanted_words = ["the", "in", "of", "and", "to", "a", "on",
                      "for", "was", "as", "from", "with", "by", "that", "at",
                      "an", "after", "which", "not", "be", "had", "is", "it"]

    for word in unwanted_words:
        if word in counts:
            del counts[word]

    total = sum([freq for (word, freq) in counts.most_common(topXwords)])

    return {word : freq / total for (word, freq) in counts.most_common(topXwords)}

def Compare(A, B):
    A_freq = GetWordsFrequency(A)
    B_freq = GetWordsFrequency(B)

    vals = [A_freq[x] * (
            1 -
             abs(B_freq[x]-A_freq[x])/A_freq[x]
             ) for x in A_freq if x in B_freq]

    print("The similarity score between " + A + " and " + B + " is " + str(sum(vals)))

Compare("Barack Obama", "Cheese")
Compare("Barack Obama", "Donald Trump")
Compare("Barack Obama", "Hillary Clinton")
Compare("Barack Obama", "Barack Obama")