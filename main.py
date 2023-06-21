import pygame
import sys

from classes.box import Box
from classes.cross_image import CrossImage

BACKGROUND_COLOR = (255, 255, 255)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WINDOW_TITLE =  "Tic Tac Toe"
BOX_SIZE = 100
BOX_PADDING = 10

box_positions = []

def create_boxes():
  total_size = BOX_SIZE + BOX_PADDING
  for row in range(3):
    for col in range(3):
      x = col * total_size
      y = row * total_size
      box = Box(screen, x, y)
      box.draw()
      box_positions.append(box)

def handle_click(mouse_pos):
  for box in box_positions:
    current_position = box.is_hovered(mouse_pos)
    if current_position:
      image = CrossImage(screen, current_position)
      image.display()

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

screen.fill(BACKGROUND_COLOR)

create_boxes()

def run_game():
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

      if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_pos = pygame.mouse.get_pos()
        handle_click(mouse_pos)

    pygame.display.update()

run_game()
