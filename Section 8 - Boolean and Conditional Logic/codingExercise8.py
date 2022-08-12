import random

print("Lucky number game. ")
lucky_number = int (random.uniform(0, 10))




userNumber = int(input("Enter your lucky number: "))

if userNumber == lucky_number:
    print("You guessed the correct number")

else:
    print(f"You did not guess the lucky number. The lucky number {lucky_number}.")