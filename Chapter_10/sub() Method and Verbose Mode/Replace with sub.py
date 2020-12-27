import re

nameRegex = re.compile(r'Agent \w+')
print(nameRegex.findall('Agent Emil said something to Agent Collins'))

# replace the pattern with the first argument in the second argument
print(nameRegex.sub('John', 'Agent Emil said something to Agent Collins'))


nameRegex = re.compile(r'Agent (\w)\w*')
print(nameRegex.findall('Agent Emil said something to Agent Collins'))

# we use r'' when we have a regex function inside:
# r'\1' keep the first letter, '\' means backslash no function of keeping
# so r'' and '' are the same thing, use r'' only with functions
print(nameRegex.sub(r'Agent \1*****', 'Agent Emil said something to Agent Collins'))

