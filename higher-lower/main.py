from art import logo, vs
from game_data import data 
import random
from replit import clear

def compare():
  if A['follower_count']>B['follower_count']:
    return 'A'
  else:
    return 'B'


def repeat():
  clear()
  print(logo)
  print(f"Compare A: {A['name']}, {A  ['description']}, {A['country']}")
  print(f"You are right. Current score is {score}")
  print(vs)
  print(f"Compare B: {B['name']}, {B  ['description']}, {B['country']}")
  
score=0
is_on=True
A=random.choice(data)
B=random.choice(data)
if A==B:
  B=random.choice(data)
else:
  while is_on:
    repeat()
    dec=input("Who has more followers? Type  'A' or 'B': ").capitalize()
    if compare()==dec:
      C=B
      A=C
      B=random.choice(data)
      score+=1
      repeat()
      
    else:
      print(f"Sorry!! You lost! Your final score is {score}")
      is_on=False