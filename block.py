import random as r
import math as m

def generateblock(limx,limy):
  x = 0
  blockX = []
  blockY = []
  layer2blockX = []
  layer3blockY = []
  prev = 0
  #layer 1 
  while(x < limx):
    x+=1
    blockX.append(x)
    current = r.randint(0,limy)
    blockY.append(current)
    prev = current
  #layer 2
  x = 0
  # while(x < limx):
  #   x+=1
  #   blockX.append(x)
  #   current = r.randint(limy,0)
  #   blockY.append(current)
  #   prev = current
  
    
    
  return(blockX,blockY)