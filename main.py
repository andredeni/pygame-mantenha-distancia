import pygame
import random
import sys

pygame.init()
window = pygame.display.set_mode([800, 580])
spaceship = pygame.image.load('spaceship.png')

imgX = 350
imgY = 400
speedX = 0
retX = random.randrange(0, 700)
retY = 0
speedret = 2
largura = 100

clock = pygame.time.Clock()
while True:
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        speedX = -10
      if event.key == pygame.K_RIGHT:
        speedX = 10
    if event.type == pygame.KEYUP:
      if (event.key == pygame.K_LEFT
        or event.key == pygame.K_RIGHT):
          speedX = 0

  window.fill((255, 255, 255))
  window.blit(spaceship, [imgX, imgY])

  pygame.draw.rect(
    window, (18, 10, 143), [retX, retY, largura, 150]
  )

  imgX += speedX
  retY += speedret

  if imgY < retY + 100 and imgY + 128 > retY:
    if imgX < retX + 100 and imgX + 128 > retX:
      sys.exit()

  if retY > 580:
    retY = 0         
    retX = random.randrange(0, 700)
    largura += 50
        
  pygame.display.update()
  clock.tick(60)