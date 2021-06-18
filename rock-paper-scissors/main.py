import random as rd
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
is_on=True
while is_on:
  move1=input("What do you chose? Type 0 for rock, 1 for paper, 2 for scissors\n")
  move1=int(move1)
  move2=rd.randint(0,2)
  moves=[rock,paper,scissors]
  print(moves[move1])
  print(f"Computers move:\n{moves[move2]}")
  if move1==move2:
    print("It's a draw!")
  elif move1==0 and move2==1:
    print("Computer wins!!")
  elif move1==0 and move2==2:
    print("You win!!")
  elif move1==1 and move2==2:
    print("Computer wins!!")
  elif move1==1 and move2==0:
    print("You win!!")
  elif move1==2 and move2==0:
    print("Computer wins!!")
  elif move1==2 and move2==1:
    print("You win!!")
  dec=input("\nDo you want to go over? Press 'y' to continue or 'n' to exit\n")
  if dec=='y':
    is_on=True
  else:
    is_on=False