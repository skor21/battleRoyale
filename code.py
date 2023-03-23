# Battle Royale Game - Day 27 and Day 28 Replit programs
import random, os, time

def dice_roll(side):
    result = random.randint(1, side)
    return result

def health():
  health_points = ((dice_roll(6)*dice_roll(12))/2)+10 # Important to not have a sub routine with the same value. If using variable with same name as sub routine, the sub routine gets deleted to make room for the variable. 
  return health_points

def strength():
  strength_points = ((dice_roll(6)*dice_roll(8))/2)+12
  return strength_points


print("Battle Royale \n")
print()
name1 = input("What name shall we call thee? \n")
print()
type1 = input("Character designation (Wizard, Orc, Human, etc.) \n")
print()
print(name1)
print(type1)
health1 = health()
strength1 = strength()
print("Health: ", health1)
print("Strength: ", strength1)
print()
print("Who will you battle to the DEATH? \n")
print()

name2 = input("What name shall we call thee? \n")
print()
type2 = input("Character designation (Wizard, Orc, Human, etc.) \n")
print()
print(name2)
print(type2)
health2 = health()
strength2 = strength()
print("Health: ", health2)
print("Strength: ", strength2)
print()

num_rounds = 1
winner = None

while True:
  time.sleep(1)
  os.system("clear")
  print("Battle Royale \n")
  print()
  print("Let the battle to the death begin! \n")

  name1_dice = dice_roll(6)
  name2_dice = dice_roll(6)

  difference = abs(strength1 - strength2) + 1 #abs or absolute gives us the positive value every single time

  if name1_dice > name2_dice:
    health2 -= difference
    if num_rounds==1:
      print(name1, "Wins the first blow")
    else:
      print(name1, "Wins round", num_rounds)
  elif name2_dice > name1_dice:
    health1 -= difference
    if round==1:
      print(name2, "Wins the first blow")
    else:
      print(name2, "Wins round", num_rounds)
      
  else:
    print("With a clickity click, the round ends in a draw. ", num_rounds)

  print()
  print(name1)
  print("Health: ", health1)
  print()
  print(name2)
  print("Health: ", health2)

  if health1 <= 0:
    print()
    print(name1, "has died! ")
    print()
    winner = name2
    break
  elif health2 <= 0:
    print()
    print(name2, "has died! ")
    print()
    winner = name1
    break
  else:
    print()
    print(name1, "and ", name2, "both survive to the next round! ")
    num_rounds += 1

time.sleep(2)
os.system("clear")
print("Battle Royale \n")
print()
print(winner, " has won in ", num_rounds, " rounds! \n")
