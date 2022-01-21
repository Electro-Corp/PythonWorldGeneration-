import random as r


def generateblock(limx,limy):
  x = 0
  blockX = []
  blockY = []
  prev = 0
  while(x < limx):
    x+=1
    blockX.append(x)
    current = r.randint((limy-15),limy)
    blockY.append(current)
    prev = current
    
    
  return(blockX,blockY)