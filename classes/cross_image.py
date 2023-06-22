from classes.image import Image

class CrossImage(Image):
  def __init__(self, screen, position, size = 80):
    super().__init__()
    self.image_name = "cross.png"
    self.size = size
    self.screen = screen
    self.position = position

  def display(self):
    self.screen.blit(super().resized_image(), (self.get_position()))

  def get_image_name(self):
    return self.image_name

  def get_position(self):
    return self.position

  def get_image_size(self):
    return self.size
