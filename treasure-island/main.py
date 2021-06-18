print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload
dir=input("You are at a cross road.Where do you want to go?. Type 'left⬅️' or 'right➡️'\n")
if dir.lower()=='left':
  act=input("You have walked long and reached a lake.\nThere is an island in the middle of the lake. Type 'wait' to wait for the boat🚣‍♂️ or type'swim' to swim🏊‍♂️ across\n")
  if act.lower()=='wait':
    door=input("You got a boat🚣‍♂️ and rowed across the lake to reach island. You have three doors at the entrance.\nType'blue'🟦 to open blue door, type'red'🟥 to open red door, type'yellow'🟨 to open yellow door.")
    if door.lower()=='yellow':
      print("You found the treasure 👑!!")
    elif door.lower()=='blue':
      print("You were eaten by a beast 👹.\nGame Over")
    elif door.lower()=='red':
      print("You were burned in fire!! 🔥\nGame Over")
    else:
      print("You entered wrong, restart the game to start from the beginning!!")
  else:
    print("You were attacked by a trout!!\nGame Over")

else:
  print("You fell into a hole. 🕳️\nGame Over")