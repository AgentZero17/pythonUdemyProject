userNumber = int(input("Please enter the number: "))

if userNumber % 2 == 1:
    print(f"Number {userNumber} is odd")
elif userNumber % 2 == 0:
    print(f"Number {userNumber} is even")
else:
    print(f"Number {userNumber} it's not a number")
    