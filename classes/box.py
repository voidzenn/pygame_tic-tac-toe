import pygame

SIZE = 100
PADDING = 10

class Box:
  def __init__(self, screen, x = 100, y = 100, size = SIZE, padding = PADDING):
    self.box = pygame.Rect(x, y, size, size)
    self.x = x
    self.y = y
    self.screen = screen
    self.size = size
    self.padding = padding

  def size(self):
    return self.size

  def x(self):
    return self.x

  def y(self):
    return self.y

  def padding(self):
    return self.padding

  def draw(self):
    pygame.draw.rect(self.screen, (255, 0, 0), self.box)

  def is_hovered(self, mouse_position):
    x = self.x
    y = self.y
    if (mouse_position[0] >= x and
      mouse_position[0] <= (x + self.size - self.padding) and
      mouse_position[1] >= y and
      mouse_position[1] <= (y + self.size - self.padding)):
        return (x, y)
