import re  # For preprocessing
from time import time  # To time our operations
import wikipedia
from collections import Counter
import logging
from functools import wraps
from nltk.stem.lancaster import LancasterStemmer

logging.basicConfig(format="%(levelname)s - %(asctime)s: %(message)s", datefmt='%H:%M:%S', level=logging.INFO)

TOP_X_WORDS = 100

def timing(function):
    @wraps(function)
    def wrap(*args, **kwargs):
        start = time()
        result = function(*args, **kwargs)
        end = time()
        logging.info("%r(%r, %r) took %2.2f secs" % (function.__name__, args, kwargs, end - start))
        return result
    return wrap

class WikiComparer:

    def __init__(self):
        self.page = ""
        self.words = []
        self.wordsByCount = {}
        self.wordsByFrequency = {}

    @timing
    def get_page_from_wiki(self, title):
        try:
            start = time()
            self.page = wikipedia.page(title).content
            end = time()
            duration_secs = round((end - start), ndigits=2)
            logging.info("First 100 characters of page: {}".format(self.page[:100]))

        except wikipedia.PageError:
            raise Exception("Unrecognised page title, please be more specific.")

    @timing
    def get_words_from_page(self):
        self.page = self.page.lower()
        self.page = re.sub('[^a-z0-9 ]', '', self.page)
        logging.info("First 100 characters of cleaned page: {}".format(self.page[:100]))

        self.words = self.page.split()
        stemmer = LancasterStemmer()
        self.words = [stemmer.stem(word) for word in self.words]
        logging.info("First 10 words: {}".format(self.words[:10]))

    def _removeStopWords(self):
        self.words = ["abc", "def"]

    def getWordsByCount(self):
        self.wordsByCount = {"abc": 1, "def": 1}

    def getWordsByFrequencyOfTopXWords(self, top_x_words):
        self.wordsByFrequency = {"abc": 0.5, "def": 0.5}
