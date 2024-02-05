import random


name= str(input("Hello! What is your name?\n"))
random_num = random.randint(1, 20)

print(f"Well, {name}, I am thinking of a number between 1 and 20\n")
number = int(input("Take a guess.\n"))

count = 1
while number != random_num:
    if number < random_num:
        print("Your guess is too low.\n")
        number = int(input("Take a guess.\n"))
        count += 1
    elif number > random_num:
        print("Your guess is too more.\n")
        number = int(input("Take a guess.\n"))
        count += 1

print(f"Good job, {name}! You guessed my number in {count} guesses!")

