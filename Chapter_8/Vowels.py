import re

string = 'You go and find the uber eats with food'
vowel = re.compile(r'[aeiouAEIOU]')
print(vowel.findall(string))

vowel = re.compile(r'[aeiouAEIOU]{2}')
print(vowel.findall(string))

consonants = re.compile(r'[^aeiouAEIOU]') # does the opposite of vowel
print(consonants.findall(string))