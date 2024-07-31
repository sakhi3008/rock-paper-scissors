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


import random 

game_images = [rock,paper,scissors]

print("Welcome to Rock-paper-Scissors game!")
user_choice = int(input("For rock-paper-scissors game choose 0 for rock,1 for paper and 2 for scissors\n"))
print(game_images[user_choice])

computer_choice = random.randint(0,2)
print("Computer choice:")
print(game_images[computer_choice])

if user_choice >= 3 and user_choice < 0:
  print("You typed an invalid number, you lose!")
elif user_choice == 0 and computer_choice == 2:
  print("You win!")
elif user_choice == 2 and computer_choice == 0:
  print("you lose!")
elif user_choice > computer_choice:
  print("You Win!")
elif computer_choice > user_choice:
  print("You lose!")
elif user_choice == computer_choice:
  print("It's a draw.")