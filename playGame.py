# Add random argument to get random library with seed
def playOneGame(random):
  numberOfRolls = 1
  playerWin = False

  sum = random.randint(1,6) + random.randint(1,6)

  if sum == 7 or sum == 11:
    playerWin = True
    return playerWin, numberOfRolls
  elif sum == 2 or sum == 3 or sum == 12:
    return playerWin, numberOfRolls

  while(True):
    numberOfRolls +=1
    sum2 = random.randint(1,6) + random.randint(1,6)
    if sum2 ==sum:
      playerWin = True
      return playerWin, numberOfRolls
    elif sum2 == 7:
      return playerWin, numberOfRolls

   
  return playerWin, numberOfRolls

# print(playOneGame())