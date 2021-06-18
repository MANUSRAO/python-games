import random 
from art import logo
def generate():
  num=random.randint(1,100)
  return num
def checker():
  if abs(guess-number)>30:
    print("Too Far Guess")
  elif abs(guess-number)>20:
    print("Far guess")
  elif abs(guess-number)>10:
    print("Near guess")
  elif abs(guess-number)<10:
    print("Very Near Guess.")
number=generate()
print(logo)
print("Welcome to the number guessing game!!\nI'm thinking of a number between 1 and 100")
dec=input("Choose a difficulty. Type 'easy' or 'hard':").lower()
if dec=='hard':
  count=5
  while count>0:
    print(f"You have {count} attempts left")
    guess=int(input("Make a guess:"))
    if guess==number:
      print(f"You got it.The number was {number}")
      count=0
    else:
      checker()
      count=count-1
else:
  count=10
  while count>0:
    print(f"You have {count} attempts left")
    guess=int(input("Make a guess:"))
    if guess==number:
      print(f"You got it.The number was {number}")
      count=0
    else:
      checker()
      count=count-1
print(f"You lost you couldn't guess the number. The number was {number}")