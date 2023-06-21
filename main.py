import pygame
import sys

from classes.box import Box

BACKGROUND_COLOR = (255, 255, 255)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WINDOW_TITLE =  "Tic Tac Toe"

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

screen.fill(BACKGROUND_COLOR)

b = Box(screen)
b.draw()

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

    if event.type == pygame.MOUSEBUTTONDOWN:
      mouse_pos = pygame.mouse.get_pos()
      print(b.is_hovered(mouse_pos))

  pygame.display.update()
