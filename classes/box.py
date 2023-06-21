import pygame

SIZE = 100
PADDING = 10
BOX_X = 100
BOX_Y = 100

class Box:
  def __init__(self, screen, size = SIZE, padding = PADDING, x = BOX_X, y = BOX_Y):
    self.box = pygame.Rect(x, y, size, size)
    self.screen = screen
    self.size = size
    self.padding = padding
    self.x = 100
    self.y = 100

  def draw(self):
    pygame.draw.rect(self.screen, (255, 0, 0), self.box)

  def is_hovered(self, mouse_position):
    if (mouse_position[0] >= self.x and
      mouse_position[0] <= (self.x + self.size - self.padding) and
      mouse_position[1] >= self.y and
      mouse_position[1] <= (self.y + self.size - self.padding)):
        return (self.x, self.y)
