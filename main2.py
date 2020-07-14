import wikipedia

obama = wikipedia.page("Barack Obama")

print(obama.content)

# see, this is a lot cleaner, a lot more like what we're expecting, and now we can work with this data
# the next thing we want to do is to separate all these words and collect it all into a frequency table
# so, for example, the number of times the word "america" appears is 100, "politics" is 50, etc

