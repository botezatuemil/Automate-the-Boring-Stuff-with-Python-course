import re
# 1 or more times

batRegex = re.compile(r'Bat(wo)+man')
mo = batRegex.search('The adventures of Batman')
try:
    print(mo.group())
except:
    print(mo)

mo = batRegex.search('The adventures of Batwowoman')
print(mo.group())