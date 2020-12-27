def spam():
    eggs = 99
    bacon()
    print(eggs)

def bacon():
    eggs = 0
    ham = 99

spam()

"""
The result is 99 not 0!!!
"""