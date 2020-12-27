import re

phoneNumberRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mo = phoneNumberRegex.search('Call me at 430-567-0000 or 654-232-8500 next Friday')
print(mo.group(1)) #430
print(mo.group(2)) #567
print(mo.group(3)) #0000