try:
  import pygame
  import time as t
  import block as b
  


except ModuleNotFoundError:
  print("Pygame not found.")
(width,height) = (360, 240)
screen = pygame.display.set_mode((width,height))
(posX,posY) = b.generateblock(width,height)
color =(0,255,0)
print(len(posX))
while True: 
  screen.fill((40,55,150))
  event = pygame.event.get()

  for event in pygame.event.get(): 
    if event.type == pygame.QUIT: 
      pygame.quit() 
  b = -1
  e = len(posX)-1
  for b in range(e) :
    b += 1
    pygame.draw.rect(screen, color, pygame.Rect(posX[b], posY[b],10,10 ))
    print("X: ",posX[b] )
    print(posY[b])

  
  pygame.display.update()