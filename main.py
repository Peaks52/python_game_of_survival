import pygame, sys


pygame.init()
screen = pygame.display.set_mode((400, 200))
pygame.display.set_caption('Selviytymispeli!')

pelaaja = pygame.Rect(200, 100, 25, 25)
vihollinen = pygame.Rect(200, 100, 40, 20)

rajahdys_kuva = pygame.image.load("kuva.png")



vihollisen_nopeus = [3,1]
FPS = 30
FramePerSec = pygame.time.Clock()

while True:

  for event in pygame.event.get():
    mouse = pygame.mouse.get_pos()
    #print(mouse)

  pelaaja = pygame.Rect(mouse[0] -13, mouse[1] -13, 26, 26)

  if vihollinen.right > 400:
    vihollisen_nopeus[0] *= -1
  if vihollinen.left < 0:
    vihollisen_nopeus[0] *= -1
  if vihollinen.bottom > 200:
    vihollisen_nopeus[1] *= -1
  if vihollinen.top < 0:
    vihollisen_nopeus[1] *= -1
    
  vihollinen.move_ip(vihollisen_nopeus)
  
  #tausta
  screen.fill("#03c6fc")
  
  #maa
  pygame.draw.rect(screen, "#369b6a", (0, 180, 400, 20))
  
  #talo
  pygame.draw.rect(screen, "RED", (220, 140, 70, 40))
  
  #katto
  pygame.draw.polygon(screen, "RED" ,[(200, 140), (255, 100), (315, 140)])
  
  #puu
  pygame.draw.rect(screen, "brown", (110, 140, 10, 40))
  pygame.draw.ellipse(screen, "#008d00", (100, 90, 30, 60))
  
  #aurinko
  pygame.draw.ellipse(screen, "gold", (10, 10, 70, 70))

  #piirretään pelaaja
  pygame.draw.rect(screen, "black", pelaaja)
  
  #piirretään vihollinen
  pygame.draw.rect(screen, "purple", vihollinen)

if (pygame.Rect.colliderect(pelaaja, vihollinen) == True):
    rajahdys_kuva = pygame.transform.scale(rajahdys_kuva, (80, 80))
    pygame.display.update()
    break
  
pygame.display.update()
FramePerSec.tick(FPS)
