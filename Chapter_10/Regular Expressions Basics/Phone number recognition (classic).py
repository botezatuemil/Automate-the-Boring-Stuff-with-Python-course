def is_phone_number(number):
    if len(number) != 12:
        return False
    for i in range(0,3):
        if not number[i].isdecimal():
            return False
    if number[3] != '-':
        return False
    for i in range(4, 7):
        if not number[i].isdecimal():
            return False
    if number[7] != '-':
        return False
    for i in range(8,12):
        if not number[i].isdecimal():
            return False
    return True

# 420-898-0000

text  = 'Call me at 430-567-0000 or 654-232-8500 next Friday'
foundNumber = False
for i in range(len(text)):
    chunck = text[i:i+12]
    if is_phone_number(chunck):
        print(chunck)
        foundNumber = True

if not foundNumber:
    print('There is no phone number')