import wikipedia
from collections import Counter

wiki = wikipedia.page("Barack Obama")

entire_page = wiki.content

entire_page_lower = entire_page.lower()

entire_page_lower_filtered = entire_page_lower

unwanted_signs = [';', ':', '!', "*", "=", ",", ".", "'s", "(", ")"]

for i in unwanted_signs :
    entire_page_lower_filtered = entire_page_lower_filtered.replace(i, '')

words = entire_page_lower_filtered.split()

counts = Counter(words)

unwanted_words = ["the", "in", "of", "and", "to", "a", "on",
                  "for", "was", "as", "from", "with", "by", "that", "at",
                  "an", "after", "which", "not", "be", "had", "is", "it"]

for word in unwanted_words:
    if word in counts:
        del counts[word]

total = sum([item[1] for item in counts.most_common(1000)])

for item, freq in counts.most_common(1000):
    print(item, '=', freq/total)


# now we've got a relative frequency. Obama is 4pc of the top 1000 words
# note, if we change the number of words from 1000 to 100, we see a different percentage. Obama is 10pc of the top 100 words. 30pc of top 10 words.
# Perhaps this can give us better accuracy to get rid of all the noisy words. This is something we can calibrate in future. So lets make this into a variable to play with in future.