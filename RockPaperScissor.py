import random

options = ["rock","paper","scissor"]

print("Rock,Paper,Scissor Game")

user_choice = input("Enter your choice(Rock,Paper,Scissor): ").lower()
computer_choice = random.choice(options)

print(f"\n you choose = {user_choice}")
print(f"computer choose = {computer_choice}")

if user_choice == computer_choice:
    print("Match Tie!")
elif (
    (user_choice == "rock" and computer_choice == "scissor") or
    (user_choice == "paper" and computer_choice == "rock") or
    (user_choice == "scissor" and computer_choice == "paper")
):
    print("You Win!")
elif user_choice in options:
    print("computer wins!")
else:
    print("Invalid Input")