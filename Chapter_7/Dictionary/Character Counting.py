import pprint
string = 'It is a nice time today, the sun shines across the field'

count = {}

for letter in string.lower():
        count.setdefault(letter, 0)
        count[letter] += 1

pprint.pprint(count)
rjtext = pprint.pformat(count)
print(rjtext)