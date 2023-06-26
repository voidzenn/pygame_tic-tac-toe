import pygame

SCREEN_WIDTH = 310
SCREEN_HEIGHT = 310
WHITE  = (255, 255, 255)
BLACK = (0, 0 ,0)
SIZE = 25
FONT_TYPE = None
SCREEN_DIMENSION = (SCREEN_HEIGHT, SCREEN_WIDTH)

class Text:
  def __init__(self, screen, screen_dimension = SCREEN_DIMENSION, text = "", size = SIZE,
              anti_alias = True, color = BLACK, font_type = FONT_TYPE):
    self.font = pygame.font.Font(font_type, size)
    self.screen = screen
    self.screen_dimension = screen_dimension
    self.text = text
    self.size = size
    self.anti_alias = anti_alias
    self.color = color
    self.font_type = font_type

  def get_screen_h(self):
    return self.screen_dimension[0]

  def get_screen_w(self):
    return self.screen_dimension[1]

  def get_text(self):
    return self.text

  def get_anti_alias(self):
    return self.anti_alias

  def get_color(self):
    return self.color

  def text_surface(self):
    return self.font.render(self.get_text(), self.get_anti_alias(), self.get_color())

  def get_text_width(self):
    return self.text_surface().get_width()

  def get_text_height(self):
    return self.text_surface().get_height()

  def screen_position(self):
    x = (self.get_screen_w() - self.get_text_width()) / 2
    y = (self.get_screen_h() - self.get_text_height()) / 2
    return (x, y)

  def box_position(self, p_left_right, p_top_bottom):
    x = (self.get_screen_w() - (self.get_text_width() + p_left_right)) / 2
    y = (self.get_screen_h() - (self.get_text_height() + p_top_bottom)) / 2
    return (x, y)

  def box_rect(self, position, p_left_right, p_top_bottom):
    width = self.get_text_width()  + p_left_right
    heigth = self.get_text_height() + p_top_bottom
    box = pygame.Rect(position[0], position[1], width, heigth)
    return box

  def draw_box(self, padding):
    # Multiply padding x and y by 2
    # Padding left should be the same as right
    # Padding top should be the same as bottom
    position = self.box_position(padding[0] * 2, padding[1] * 2)
    box = self.box_rect(position, padding[0] * 2, padding[1] * 2)
    return pygame.draw.rect(self.screen, WHITE, box)

  def display(self):
    self.screen.blit(self.text_surface(), (self.screen_position()))

  def display_text_box(self, padding = (10, 10)):
    self.draw_box(padding)
    self.screen.blit(self.text_surface(), (self.screen_position()))
