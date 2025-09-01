import random
choices = ["rock", "paper", "scissors"]

print("Rock Paper Scissors Game")

while True:
    user_choice = input("Enter your choice (rock/paper/scissors or exit): ").lower()

    if user_choice == "exit":
        print("Thanks for playing")
        break

    if user_choice not in choices:
        print("Invalid choice!! Please type rock, paper, or scissors.\n")
        continue

    computer_choice = random.choice(choices)

    print("You chose:", user_choice)
    print("Computer chose:", computer_choice)

    if user_choice == computer_choice:
        print("It's a tie!\n")
    elif user_choice == "rock" and computer_choice == "scissors":
        print("You win! Rock breaks Scissors\n")
    elif user_choice == "paper" and computer_choice == "rock":
        print("You win! Paper covers Rock\n")
    elif user_choice == "scissors" and computer_choice == "paper":
        print("You win! Scissors cut Paper\n")
    else:
        print("Computer wins!\n")
