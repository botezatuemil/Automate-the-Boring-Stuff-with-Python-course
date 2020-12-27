import re, pyperclip

# TODO: make the regex for phone numbers

phoneRegex = re.compile(r'''
# 423-454-0000, 555-0000, (324) 345-0000, 555-0000 ext 12345, ext. 12345, x12345

(
((\d\d\d)|(\(\d\d\d\)))?       # area code
(\s|-)                         # first separator
\d\d\d                         # first 3 digits
-                              # separator
\d\d\d\d                       # last 4 digits
(((ext(\.)?\s)|x) (\d{2,5}))?  # extension (optional)
)
''', re.VERBOSE) # VERBOSE used for commenting

# TODO: make the regex for email addresses

emailRegex = re.compile(r'''
# something+._@something.com

[a-zA-Z0-9_.+]+       # name 
@                     # @ symbol
[a-zA-Z0-9_.+]+       # domanin name part

''', re.VERBOSE)

# TODO: get the text of the clipboard

text = pyperclip.paste()

# TODO: extract the email addresses and the phone numbers

extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumbers in extractedPhone:
    allPhoneNumbers.append(phoneNumbers[0])

print(allPhoneNumbers)
print(extractedEmail)

# TODO: copy the extracted to the clipboard
# use x.join(list): concatenate x at every element of the list
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)




