import pygame

ROOT_PATH = "assets/images"

class Image:
  def load_file(self):
    try:
      path = ROOT_PATH + "/" + self.get_name()
      return pygame.image.load(path)
    except FileNotFoundError:
      print("File cannot be found")

  def resized_image(self):
    size = self.get_size()
    return pygame.transform.scale(self.load_file(), (size, size))

  def center_image_size(self, padding):
    pos = self.get_position()
    x = pos[0] + (padding * 2)
    y = pos[1] + (padding * 2)

    return (x, y)

  def get_name(self):
    return self.get_image_name()

  def get_size(self):
    return self.get_image_size()

