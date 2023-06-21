import pygame
import sys

BACKGROUND_COLOR = (255, 255, 255)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WINDOW_TITLE =  "Tic Tac Toe"

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

screen.fill(BACKGROUND_COLOR)

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
  pygame.display.update()
