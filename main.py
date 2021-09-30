from playGame import playOneGame
from analysis import playNTimes,plotSimulation

# Input number of games and the seed 
numGames = int(input("Enter the number of games "))
try:
  seed = int(input("Enter the seed "))
except ValueError:
  seed =-1
# Simulate 
winThrows,lostThrows = playNTimes(playOneGame,numGames,seed)
# Plot the simulation results
plotSimulation(winThrows,lostThrows,numGames)

# I hope that helps you out
# Saved the figure for you, you can use it. It is stored in Figure_1.png
# You can resize the code editor as well using dragging the right border 

