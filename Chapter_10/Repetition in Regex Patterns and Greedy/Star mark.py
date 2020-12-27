import re
# 0 or more times
batRegex = re.compile(r'Bat(wo)*man')

mo = batRegex.search('The adventures of Batman')
print(mo.group())

mo = batRegex.search('The adventure of Batwowoman')
print(mo.group())