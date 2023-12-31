import pygame
import sys

from classes.game import Game
from classes.box import Box
from classes.cross_image import CrossImage
from classes.circle_image import CircleImage
from classes.text import Text

BACKGROUND_COLOR = (255, 255, 255)
SCREEN_WIDTH = 310
SCREEN_HEIGHT = 310
WINDOW_TITLE =  "Tic Tac Toe"
BOX_SIZE = 100
BOX_PADDING = 5

def create_boxes():
  box_positions = []
  total_size = BOX_SIZE + BOX_PADDING
  for row in range(3):
    for col in range(3):
      x = col * total_size
      y = row * total_size
      box = Box(screen, x, y)
      box.draw()
      box_positions.append(box)
  return box_positions

def load_circle(position):
  image = CircleImage(screen, position)
  image.display_centered(BOX_PADDING)

def load_cross(position):
  image = CrossImage(screen, position)
  image.display_centered(BOX_PADDING)

def handle_image(position, index, game):
  selected_boxes = game.get_selected_boxes()
  if position not in selected_boxes:
    if game.is_current_turn_circle():
      load_circle(position)
      game.set_previous_turn_cross()
      game.add_circle_selection(index)
    elif not game.is_current_turn_circle():
      load_cross(position)
      game.set_previous_turn_circle()
      game.add_cross_selection(index)

    game.add_position(position)

def handle_click(mouse_pos, game, box_positions):
  for index, box in enumerate(box_positions):
    current_position = box.is_hovered(mouse_pos)
    if current_position:
      handle_image(current_position, index, game)

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

screen.fill(BACKGROUND_COLOR)

def run_game():
  screen.fill(BACKGROUND_COLOR)

  game = Game()
  box_positions = create_boxes()
  text = Text(screen, (SCREEN_HEIGHT, SCREEN_WIDTH))

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

      if event.type == pygame.MOUSEBUTTONDOWN:
        if not game.is_ended():
          count = game.get_count_selected_boxes()
          if count < len(box_positions):
            mouse_pos = pygame.mouse.get_pos()
            handle_click(mouse_pos, game, box_positions)
        if game.is_ended():
          run_game()

      if event.type == pygame.MOUSEBUTTONUP:
        if not game.is_ended():
          if game.is_circle_won() or game.is_cross_won():
            game.end()
            text.set_text(game.check_winner())
            text.display_text_box()
          elif game.get_count_selected_boxes() == len(box_positions):
            game.end()
            text.set_text("No winner, click again to restart")
            text.display_text_box()
    pygame.display.update()

run_game()
