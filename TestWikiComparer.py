import unittest
from wikiCompare.WikiComparer import WikiComparer


class TestWikiComparer(unittest.TestCase):
    def test_get_words_from_wiki(self):
        wikiComparer = WikiComparer()
        wikiComparer.get_page_from_wiki("Barack Obama")
        expected_minimum_size_of_page = 100
        self.assertGreater(len(wikiComparer.page), expected_minimum_size_of_page)

    def test_get_words_from_page(self):
        wikiComparer = WikiComparer()
        wikiComparer.page = "Dog Dog's Dogs dog dog, dog! dogging dogged"
        wikiComparer.get_words_from_page()
        expected_words = ["dog", "dog", "dog", "dog", "dog", "dog", "dog", "dog"]
        self.assertEqual(wikiComparer.words, expected_words)

if __name__ == '__main__':
    unittest.main()
