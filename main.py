import random
import game_data
import art
from replit import clear

a = random.choice(game_data.data)

score = 0
play = True

while (play):
  b = random.choice(game_data.data)

  print(art.logo)
  if (score > 0):
    print("You're right! Current score: ", score)

  print("Compare A: ", a["name"], ",", a["description"], ",from", a["country"],
        ".")

  print(art.vs)
  print("Against B: ", b["name"], ",", b["description"], ",from", b["country"],
        ".")
  print("Who has more follower ?  Type A or B")
  ans = (input())

  if (ans == "A" and a["follower_count"] >= b["follower_count"]):
    score += 1
  elif (ans == "B" and b["follower_count"] >= a["follower_count"]):
    score += 1
    a = b

  else:
    play = False

  clear()

print("Sorry, that's wrong. Final score: ", score)
