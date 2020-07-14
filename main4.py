import wikipedia

wiki = wikipedia.page("Barack Obama")

entire_page = wiki.content

words = entire_page.split() #read the words into a list.

print(words)

# we've now taken all the words and split it, and now lets make it into a frequency table