import random

print('Hello what is your name?')
name = input()
print("Well " + name + ", I am thinking of a number between 1 and 10")

secret_number = random.randint(1, 10)

for i in range(3):
    my_number = int(input("Number: "))
    if my_number > secret_number:
        print("Your guess is too high")
    elif my_number < secret_number:
        print("Your guess is too low")
    else:
        break

if my_number == secret_number:
    print("Congrats the number is " + str(my_number))
else:
    print("You lost, the number was " + str(secret_number))

