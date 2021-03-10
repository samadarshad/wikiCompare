import re

import numpy
import wikipedia
from collections import Counter
import logging
from nltk.stem.lancaster import LancasterStemmer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

from wikiCompare.utils import timing

logging.basicConfig(format="%(levelname)s - %(asctime)s: %(message)s", datefmt='%H:%M:%S', level=logging.INFO)

TOP_X_WORDS = 100
stop_words = set(stopwords.words('english'))


def calculate_score_between_frequency(a, b):
    return min(a, b)
    # note that this is an imperfect method for calculating the similarity between two frequency tables. A more suitable method would be a chi-squared test or something.


class WikiComparer:

    @timing
    def get_page_from_wiki(self, title):
        try:
            page = wikipedia.page(title).content
            logging.info("First 100 characters of page: {}".format(page[:100]))
            return page

        except wikipedia.PageError:
            raise Exception("Unrecognised page title, please be more specific.")

    @timing
    def get_words_from_page(self, page):
        page = page.lower()
        page = re.sub('[^a-z0-9 ]', '', page)
        logging.info("First 100 characters of cleaned page: {}".format(page[:100]))

        words = word_tokenize(page)
        stemmer = LancasterStemmer()
        words = [stemmer.stem(word) for word in words]
        logging.info("First 10 words: {}".format(words[:10]))
        return words

    @timing
    def remove_stop_words(self, words):
        return [word for word in words if word not in stop_words]

    @timing
    def get_words_by_count(self, words):
        return Counter(words)

    @timing
    def get_words_by_frequency(self, words_by_count, top_x_words):
        top_words = Counter(words_by_count).most_common(top_x_words)
        total = sum([freq for (word, freq) in top_words])
        return {word: freq / total for (word, freq) in top_words}

    @timing
    def get_words_frequency_of_page(self, title):
        page = self.get_page_from_wiki(title)
        words = self.get_words_from_page(page)
        words = self.remove_stop_words(words)
        words_by_count = self.get_words_by_count(words)
        words_by_freq = self.get_words_by_frequency(words_by_count, TOP_X_WORDS)
        logging.info("Top 10 words and their frequencies: {}".format(Counter(words_by_freq).most_common(10)))
        return words_by_freq

    @timing
    def calculate_similarity(self, word_freq_a, word_freq_b):
        similarity_score = {x: calculate_score_between_frequency(word_freq_a[x], word_freq_b[x])
                            for x in word_freq_a if x in word_freq_b}
        score = sum(similarity_score.values())
        return score
