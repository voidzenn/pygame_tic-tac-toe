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

  def display_centered(self, box_padding):
    size = super().center_image_size(box_padding)
    self.screen.blit(super().resized_image(), size)

  def get_image_name(self):
    return self.image_name

  def get_position(self):
    return self.position

  def get_image_size(self):
    return self.size

  def get_padding(self):
    return self.padding
