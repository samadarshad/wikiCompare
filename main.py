from urllib.request import urlopen

url = "https://en.wikipedia.org/wiki/Barack_Obama"
html = urlopen(url).read()
print(html[1:50000])

# look for: is an American politician and attorney who served as the 44th
# its printing the website out, but its got all this crap

# what we're interested in are getting these words out, "american", "politician", "attorney", these are the valuable things that can give us the feature of this page
# the other html stuff we dont want
# so firstly we gotta get rid of all that and only focus on the good bits
# this means writing some code to go through all this data, getting rid of all the crap, keeping only the good
# but fortunately, someone has already done this
# we're gonna steal his code and use it in our program
