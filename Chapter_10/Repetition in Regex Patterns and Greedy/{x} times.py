import re
# exactly x times

laugh = re.compile(r'(Ha){3}')
mo = laugh.search('HaHaHa')
print(mo.group())

phone = re.compile(r'(\d\d\d-\d\d\d-\d\d\d\d(,)?){3}')
mo = phone.search('234-435-3454,324-454-2342,324-454-3425')
print(mo.group())
