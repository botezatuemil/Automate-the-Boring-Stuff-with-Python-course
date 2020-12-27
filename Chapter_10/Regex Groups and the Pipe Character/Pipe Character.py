import re

batRegex = re.compile(r'Bat(man|mobile|cycle)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())