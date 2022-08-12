from random import choice, randint

flag = False
print("Rock, Paper, Scissors - Game")
computerChoice = choice(["Rock", "Paper", "Scissors"])
computerChoice = computerChoice.lower()

while flag is False:
    userChoice = str(input("Please enter your choice ")).lower()
    if userChoice == "rock" or userChoice == "paper" or userChoice == "scissors":
        flag = True
    else:
        print(f"{userChoice} invalid input")
        flag = False


if userChoice:
    print(f"Computer chose: {computerChoice}")
    if userChoice == computerChoice:
        print("It's a tie!\nPlease play again.")
    elif userChoice == "rock" and computerChoice == "paper":
        print("Computer wins")
    elif userChoice == "paper" and computerChoice == "scissors":
        print("Computer wins")
    elif userChoice == "scissors" and computerChoice == "rock":
        print("Computer Wins")
    else:
        print("You win!!")
