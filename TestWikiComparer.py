import unittest
from unittest import mock
from unittest.mock import patch

from parameterized import parameterized

from wikiCompare.WikiComparer import WikiComparer


class TestWikiComparer(unittest.TestCase):
    @patch('wikiCompare.WikiComparer.wikipedia')
    def test_get_words_from_wiki(self, mock_wiki):
        mock_wiki_page = "hello abc"
        mock_wiki.page().content = mock_wiki_page
        wikiComparer = WikiComparer()
        page = wikiComparer.get_page_from_wiki("Page Title")
        self.assertEqual(page, mock_wiki_page)

    def test_remove_stop_words(self):
        wikiComparer = WikiComparer()
        words = ["the", "dog", "was", "happy"]
        expected_words = ["dog", "happy"]
        clean_words = wikiComparer.remove_stop_words(words)
        self.assertEqual(clean_words, expected_words)

    @parameterized.expand([
        ["obama", "obama president", ["obam", "presid"]],  # stem removes the last bit of the word
        ["dog", "Dog Dog's Dogs dog dog, dog! dogging dogged", ["dog", "dog", "dog", "dog", "dog", "dog", "dog", "dog"]]
    ])
    def test_get_words_from_page(self, name, page, expected_words):
        wikiComparer = WikiComparer()
        words = wikiComparer.get_words_from_page(page)
        self.assertEqual(words, expected_words)

    def test_get_words_by_count(self):
        wikiComparer = WikiComparer()
        words = ["a", "b", "a", "c"]
        expected_word_counts = {"a": 2, "b": 1, "c": 1}
        words_by_count = wikiComparer.get_words_by_count(words)
        self.assertEqual(words_by_count, expected_word_counts)

    def test_get_words_by_frequency(self):
        wikiComparer = WikiComparer()
        words_by_count = {"a": 2, "b": 1, "c": 1}
        expected_word_frequencies = {"a": 0.5, "b": 0.25, "c": 0.25}
        words_by_frequency = wikiComparer.get_words_by_frequency(words_by_count, 3)
        self.assertEqual(words_by_frequency, expected_word_frequencies)

    @patch('wikiCompare.WikiComparer.wikipedia')
    def test_get_words_frequency_of_page(self, mock_wiki):
        mock_wiki_page = "Hello, hello! Running run runner"
        mock_wiki.page().content = mock_wiki_page
        wikiComparer = WikiComparer()
        words_by_frequency = wikiComparer.get_words_frequency_of_page("Page title")
        expected_word_frequencies = {"hello": 0.4, "run": 0.6}
        self.assertEqual(words_by_frequency, expected_word_frequencies)

    @parameterized.expand([
        ["similar_100pc", {"hello": 0.4, "run": 0.6}, {"hello": 0.4, "run": 0.6}, {"hello": 0.4, "run": 0.6}],
        ["similar_60pc", {"hello": 0.4, "run": 0.6}, {"hello": 0.0, "run": 0.6}, {"hello": 0.0, "run": 0.6}],
        ["similar_0pc", {"hello": 0.4, "run": 0.0}, {"hello": 0.0, "run": 0.6}, {"hello": 0.0, "run": 0.0}],
    ])
    def test_get_most_common_shared_words(self, name, a, b, expected_common_words):
        wikiComparer = WikiComparer()
        common_words = wikiComparer.get_compared_words(a, b)
        self.assertEqual(common_words, expected_common_words)

    @parameterized.expand([
        ["similar_100pc", {"hello": 0.4, "run": 0.6}, 1],
        ["similar_60pc", {"hello": 0.0, "run": 0.6}, 0.6],
        ["similar_0pc", {"hello": 0.0, "run": 0.0}, 0.0],
    ])
    def test_calculate_similarity(self, name, compared_words, expected_similarity):
        wikiComparer = WikiComparer()
        similarity = wikiComparer.calculate_similarity(compared_words)
        self.assertEqual(similarity, expected_similarity)

    @parameterized.expand([
        ["similar_100pc", "Hello, hello! Running run runner", "Hello, hello! Running run runner", 1],
        ["similar_60pc", "Hello, hello! Running run runner", "Running run runner", 0.6],
        ["similar_0pc", "Hello, hello!", "Running run runner", 0.0],
    ])
    @patch('wikiCompare.WikiComparer.wikipedia')
    def test_compare_pages(self, name, mock_wiki_page_a, mock_wiki_page_b, expected_score, mock_wiki):
        def load_mock_data(page_title, *args, **kwargs):
            obj = mock.Mock()
            if page_title == "Page title A":
                obj.content = mock_wiki_page_a
            elif page_title == "Page title B":
                obj.content = mock_wiki_page_b
            return obj

        mock_wiki.page.side_effect = load_mock_data

        wikiComparer = WikiComparer()
        score = wikiComparer.compare_pages("Page title A", "Page title B")
        self.assertEqual(score, expected_score)

if __name__ == '__main__':
    unittest.main()
