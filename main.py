import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
comp_choice = random.randint(0,2)

game_images = [rock, paper, scissors]
game_choices = ["rock", "paper", "scissors"]
choice_list = [game_images, game_choices]

print(f"You chose: {choice_list[1][user_choice]}")
print(f"{choice_list[0][user_choice]}")

print(f"The computer chose: {choice_list[1][comp_choice]}")
print(f"{choice_list[0][comp_choice]}")

if user_choice == comp_choice:
  print("Its a DRAW.")
elif user_choice == 0 and comp_choice == 2:
  print("YOU WIN!")
elif user_choice == 2 and comp_choice == 0:
  print("You Lose.")
elif user_choice < comp_choice:
  print("You Lose")
elif user_choice > comp_choice:
  print("YOU WIN!")
elif user_choice > 2:
  print("Error: Choose either 0, 1, or 2")