import wikipedia
from collections import Counter
import re

topXwords = 1000

stop_words = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd",
              'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers',
              'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what',
              'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was',
              'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an',
              'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with',
              'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to',
              'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once',
              'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most',
              'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's',
              't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're',
              've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't",
              'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't",
              'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't",
              'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]


def GetWordsFrequency(page_title):
    try:
        page = wikipedia.page(page_title)
    except:
        raise("Unrecognised page title, please be more specific.")

    page = page.content.lower()

    page = re.sub('[^a-z0-9 ]', '', page)

    words = page.split()

    counts = Counter(words)

    # unwanted_words = ["the", "in", "of", "and", "to", "a", "on",
    #                   "for", "was", "as", "from", "with", "by", "that", "at",
    #                   "an", "after", "which", "not", "be", "had", "is", "it",
    #                   "also", "during", "who", "were", "their", "where", "his",
    #                   "about", "he", "she", "her", "them", "its", "they", "has",
    #                   "are", "have", "most"
    #                   ]

    filteredWords = {word: num for (word, num) in counts.items() if not word in stop_words}

    filteredWords = Counter(filteredWords)

    # for item, freq in filteredWords.most_common(topXwords):
    #     print(item, '=', freq )

    total = sum([freq for (word, freq) in filteredWords.most_common(topXwords)])

    return {word: freq / total for (word, freq) in filteredWords.most_common(topXwords)}


def CalculateScoreBetween(a, b):
    return min(a, b)
    # note that this is an imperfect method for calculating the similarity between two frequency tables. A more suitable method would be a chi-squared test or something.


def Compare(titleA, titleB):
    A = GetWordsFrequency(titleA)
    B = GetWordsFrequency(titleB)

    comparedWords = {x: CalculateScoreBetween(A[x], B[x]) for x in A if x in B}

    score = sum(comparedWords.values())

    print("The similarity score between " + titleA + " and " + titleB + " is " + str(score))
    print("The most common words are:")
    print([word for (word, freq) in Counter(comparedWords).most_common(10)])
    print("")


Compare("Barack Obama", "Barack Obama")
Compare("Barack Obama", "Donald Trump")
Compare("Barack Obama", "Cheese")
Compare("Pakistan", "China")
Compare("Pakistan", "India")
Compare("India", "Modi")