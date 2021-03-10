import unittest
from wikiCompare.WikiComparer import WikiComparer

class SanityTests(unittest.TestCase):
    def test_same_page(self):
        wikiComparer = WikiComparer()
        score = wikiComparer.compare_pages("Barack Obama", "Barack Obama")
        self.assertGreater(score, 0.99)

    def test_similar_topic_vs_different_topic(self):
        wikiComparer = WikiComparer()
        us_presidents_score = wikiComparer.compare_pages("Barack Obama", "Donald Trump")
        president_vs_cheese_score = wikiComparer.compare_pages("Barack Obama", "Cheese")
        self.assertGreater(us_presidents_score, president_vs_cheese_score)


if __name__ == '__main__':
    unittest.main()
