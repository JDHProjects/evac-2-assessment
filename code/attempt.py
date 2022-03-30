import random

INITIAL_GROUP = 25
groups = []
for i in range(0,4):
  for _ in range(0,INITIAL_GROUP):
    groups.append({"wealth":0,"group":i})

def getPayoff(defender, attacker):
  if(defender == 0):
    if (attacker == 0): return 4
    if (attacker == 1): return 0
    if (attacker == 2): return 4
    if (attacker == 3): return 0
  if(defender == 1):
    if (attacker == 0): return 6
    if (attacker == 1): return 4
    if (attacker == 2): return 6
    if (attacker == 3): return 1
  if(defender == 2):
    if (attacker == 0): return 4
    if (attacker == 1): return 0
    if (attacker == 2): return 1
    if (attacker == 3): return 0
  if(defender == 3):
    if (attacker == 0): return 6
    if (attacker == 1): return 1
    if (attacker == 2): return 6
    if (attacker == 3): return 0


import numpy as np
import matplotlib.pyplot as plt

plt.axis([0, 10, 0, 1])
xaxis = []
yaxis = []
for i in range(10):
  xaxis.append(i)
  y = np.random.random()
  yaxis.append(y)
  plt.cla()
  plt.plot(xaxis, yaxis)
  plt.pause(0.05)

plt.show()

def plotGroups(groups):
  pass
'''
for i in range(0,100):
  selection = random.sample(range(0,len(groups)),2)
  groups[selection[0]]["wealth"] += getPayoff(groups[selection[0]]["group"],groups[selection[1]]["group"])
  groups[selection[1]]["wealth"] += getPayoff(groups[selection[1]]["group"],groups[selection[0]]["group"])
  print(groups)'''