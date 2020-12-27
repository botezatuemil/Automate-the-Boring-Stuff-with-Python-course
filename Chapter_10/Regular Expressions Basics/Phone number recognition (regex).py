import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('Call me at 430-567-0000 or 654-232-8500 next Friday')
print(mo.group())
print(phoneNumRegex.findall('Call me at 430-567-0000 or 654-232-8500 next Friday'))