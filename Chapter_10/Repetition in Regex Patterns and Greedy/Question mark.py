import re
# 0 or 1 times
batRegex = re.compile(r'Bat(wo)?man')

mo = batRegex.search('The adventures of Batman')
print(mo.group())

mo = batRegex.search('The adventures of Batwoman')
print(mo.group())


mo = batRegex.search('The adventures of Batwowoman')
try:
    print(mo.group())
except:
    print(mo)