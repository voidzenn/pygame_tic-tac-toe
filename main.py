import pygame
import sys

from classes.game import Game
from classes.box import Box
from classes.cross_image import CrossImage
from classes.circle_image import CircleImage

BACKGROUND_COLOR = (255, 255, 255)
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 300
WINDOW_TITLE =  "Tic Tac Toe"
BOX_SIZE = 100
BOX_PADDING = 5

box_positions = []
selected_boxes = []
game = Game()

def create_boxes():
  total_size = BOX_SIZE + BOX_PADDING
  for row in range(3):
    for col in range(3):
      x = col * total_size
      y = row * total_size
      box = Box(screen, x, y)
      box.draw()
      box_positions.append(box)

def load_circle(position):
  image = CircleImage(screen, position)
  image.display()

def load_cross(position):
  image = CrossImage(screen, position)
  image.display()

def handle_image(position):
  selected_boxes = game.get_selected_boxes()
  if position not in selected_boxes:
    if game.is_current_turn_circle():
      load_circle(position)
      game.set_previous_turn_cross()
    elif not game.is_current_turn_circle():
      load_cross(position)
      game.set_previous_turn_circle()

    game.add_position(position)

def handle_click(mouse_pos):
  for box in box_positions:
    current_position = box.is_hovered(mouse_pos)
    if current_position:
      handle_image(current_position)

def initialize_game():
  create_boxes()

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

screen.fill(BACKGROUND_COLOR)

def run_game():
  initialize_game()

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
