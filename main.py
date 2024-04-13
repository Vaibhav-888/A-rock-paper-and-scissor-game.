# A-rock-paper-and-scissor-game.
It is a simple rock paper and scissor game.
import random

# Rock Paper Scissors ASCII Art

Rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

Paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""


Scissors =  """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

def lets_play():
        
my_choice = int(input("Please chose your option. 0 for rock, 1 for paper, 2 for scissor:\n"))

comp_choice = random.randint(0,2)

x = [Rock, Paper, Scissors]

print(f"You chose {my_choice} {x[my_choice]}")
print(f"Machine chose {comp_choice} {x[comp_choice]}")

if my_choice >= 3 and my_choice < 0:
    print("You choose an invalid choice.\n Machine Wins!")
elif my_choice == 0 and comp_choice == 1:
    print("You Won!")
elif my_choice == 1 and comp_choice == 2:
    print("Machine won. \n Better luck next time.")
elif my_choice == 2 and comp_choice == 0:
    print("Machine won. \n Better luck next time.")
elif my_choice == 0 and comp_choice == 0:
    print("It's a draw!")
elif my_choice == 1 and comp_choice == 1:
    print("It's a draw!")
elif my_choice == 2 and comp_choice == 2:
    print("It's a draw!")
else:
    print("Game finished!")
    




# y = []


    
    # print(x)
    # print(comp_choise)
    # print(my_choise)
    



    
    
