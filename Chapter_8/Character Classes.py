import re

lyrics = '12 drummers and 34 bassist and 4 people with 5 soda for each'
xmaxRegex = re.compile(r'\d+\s\w+')
print(xmaxRegex.findall(lyrics))