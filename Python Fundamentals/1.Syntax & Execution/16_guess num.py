import random
number = random.randint(1, 20)
guess = int(input("Guess a number: "))
print("Number was:", number)
print("Correct:", guess == number)