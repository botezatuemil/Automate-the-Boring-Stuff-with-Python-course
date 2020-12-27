import random

heads = 0
for i in range(1001):
    heads += random.randint(0, 1)
    if i == 500:
        print('Halfaway done!')

print('Heads came up ' + str(heads) + ' times.')
