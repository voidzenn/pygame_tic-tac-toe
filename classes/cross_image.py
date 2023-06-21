from classes.image import Image

class CrossImage(Image):
  def __init__(self, screen, position, size = 80):
    super().__init__()
    self.image_load = super().image_load("cross.png")
    self.size = size
    self.screen = screen
    self.position = position

  def get_resized_image(self):
    return super().resized_image(self.image_load, self.size, self.size)

  def get_rect(self):
    return self.get_resized_image().get_rect()

  def display(self):
    self.screen.blit(self.get_resized_image(), (self.position))
