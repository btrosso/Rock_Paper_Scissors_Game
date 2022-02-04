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

key = [[1, rock, "rock"], [2, paper, "paper"], [3, scissors, "scissors"]]

print(f"You chose: {key[user_choice][2]}")
print(f"{key[user_choice][1]}")
print(f"The computer chose: {key[comp_choice][2]}")
print(f"{key[comp_choice][1]}")

if user_choice == comp_choice:
  print("Its a DRAW.")
else:
  if user_choice == 1:
    if comp_choice == 2:
      print("You Lose.")
    else:
      print("You Win!")
  elif user_choice == 2:
    if comp_choice == 3:
      print("You Lose.")
    else:
      print("You Win!")
  else:
    if comp_choice == 1:
      print("You Lose.")
    else:
      print("You Win!")