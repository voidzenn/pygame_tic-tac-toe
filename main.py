import pygame
import sys

from classes.box import Box

BACKGROUND_COLOR = (255, 255, 255)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WINDOW_TITLE =  "Tic Tac Toe"

box_positions = []

def create_boxes():
  for row in range(3):
    for col in range(3):
      x = col * (100 + 10)
      y = row * (100 + 10)
      box = Box(screen, x, y)
      box.draw()
      box_positions.append(box)

def handle_click(mouse_pos):
  for box in box_positions:
    current_position = box.is_hovered(mouse_pos)

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
