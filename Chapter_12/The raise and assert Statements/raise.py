import os, traceback

"""
*************
*           *
*           *   
*           *
*************
"""

def box(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('Enter string of length 1!')
    if width < 2 or height < 2:
        raise Exception('Enter width and height greater than 1!')
    print(symbol * width)

    for i in range(height):
        print(symbol + ' ' * (width - 2) + symbol)

    print(symbol * width)

box('*', 4, 3)

try:
    raise Exception('This is error message')
except:
    errorFile = open('error_log.txt', 'a')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info was written in error_log.txt')

print(os.getcwd())