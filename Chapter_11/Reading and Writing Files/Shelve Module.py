import shelve
# use shelve for binary storage, a cheap memory storage

shelfFile = shelve.open('mydata')
shelfFile['colors'] = ['Black', 'Red', 'Yellow', 'Blue']
print(shelfFile['colors'])

# Methods
print(list(shelfFile.keys()))
print(list(shelfFile.values()))