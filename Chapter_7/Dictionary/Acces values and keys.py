car = {'name': 'Paseratti', 'km': 300000, 'age': 2001}

print(car['name'])

for k in car.keys():
    print(k)

for k in car.values():
    print(k)

for k, v in car.items():
    print(k, v)

if 'name' in car.keys():
    print("Got it")
else:
    print("Not here")

print('km' in car.values())