import matplotlib.pyplot as plt
import random
plt.rcParams["figure.figsize"] = (5,10)
def playNTimes(playOneGame,numGames,seed):
  winThrows = []
  lostThrows = []
  if seed != -1:
    random.seed(seed)
  for _ in range(numGames):
    result,throws = playOneGame(random)
    winThrows.append(throws) if result else lostThrows.append(throws)
  return (winThrows,lostThrows)
def plotSimulation(winThrows,lostThrows,numGames):
  throws = set(winThrows) | set(lostThrows)
  winPercent = [(winThrows.count(throw)/numGames)*100 for throw in throws]
  lostPercent = [(lostThrows.count(throw)/numGames)*100 for throw in throws]
  fig, ax1 = plt.subplots()
  ax2 = ax1.twinx()
  ax1.plot(list(throws),winPercent,'r--',label="Win Percentage")
  ax2.plot(list(throws),lostPercent,'g--',label="Loss Percentage")
  ax1.set_xlabel("Number of Throws")
  ax1.set_ylabel("Percentage of the total number of games\n that terminate in a win versus\n # of throws",color='r')
  ax2.set_ylabel("Percentage of the total number of games\n that terminate in a loss versus\n # of throws",color='g')
  ax1.set_title("Simulation results")
  plt.show()
  


  


