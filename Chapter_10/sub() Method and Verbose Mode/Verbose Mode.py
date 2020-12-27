import re

regex = re.compile(r'''
\d\d\d|
\(\d\d\d\)
-?
\d\d\d
-?
\d\d\d\d
''', re.VERBOSE | re.DOTALL | re.I)
print(regex.findall('342-234-2003 , 369-(324) 0000, 334 289 3432'))
