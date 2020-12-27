import re

regex = re.compile(r'^Hello')
print(regex.findall('Hello world!'))

regex = re.compile(r'Hello$')
print(regex.findall('He said Hello'))

regex = re.compile(r'^\d+$')
print(regex.findall('123456'))

regex = re.compile(r'.at') # '.' works for everything except for newline character
print(regex.findall('The cat sat on the flat mat')) # the dot character looking for a single character before '.'

regex = re.compile(r'.{1,2}at')
print(regex.findall('The cat sat on the flat mat'))

regex = re.compile(r'First name: (.*) Last name: (.*)')
print(regex.findall('First name: Emil Last name: Botezatu'))

nonGreedy = re.compile(r'<.*?>') # match the first pattern
print(nonGreedy.findall('<To serve humans> for dinner>'))

greedy = re.compile(r'<.*>') # match until final
print(greedy.findall('<To serve humans> for dinner>'))

regex = re.compile(r'.*', re.DOTALL) # truly all characters
print(regex.search('To serve humans \n for different purposes \n regarding the diet'))

regex = re.compile(r'[aeiou]', re.I) # matching case insensitive        
print(regex.findall('This is what I wanted'))

