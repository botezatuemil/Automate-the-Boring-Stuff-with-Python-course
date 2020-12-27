import re

password = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])[A-Za-z0-9!?#@%^&*]{8,}')
myPassword = input('Enter your password: ')
print(password.findall(myPassword))