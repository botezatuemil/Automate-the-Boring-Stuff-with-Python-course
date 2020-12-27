import re

# at least x times, maximum y times
# it works like slices: {,5} ; {2,}

number = re.compile(r'(\d){3,5}')
mo = number.search('0123456789') # greedy matching match the longest string possible
print(mo.group())

number = re.compile(r'(\d){3,5}?')
mo = number.search('0123456789') # non-greedy matching match the shortest string possible
print(mo.group())
