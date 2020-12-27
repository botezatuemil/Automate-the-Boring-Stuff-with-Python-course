import re
# Se da un sir de caractere. Sa se numere cate parole de forma #*?d!*+ exista, unde d este o cifra

passwordRegex = re.compile(r'\#\*\?\d\!\*\+')
count = 0
string = '#*?4!*+ este o parola ca #*?5!*+ si puternica ca #*?3!*+'

mo = passwordRegex.findall(string)

print(mo)
