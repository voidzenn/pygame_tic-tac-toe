import pygame

class Image:
  def __init__(self):
    self.root_path = "assets/images"

  def image_load(self, img_name):
    try:
      path = self.root_path + "/" + img_name
      return pygame.image.load(path)
    except FileNotFoundError:
      print("File cannot be found")

  def resized_image(self, image, x, y):
    return pygame.transform.scale(image, (x, y))

  def get_rect(self, image):
    return image.get_rect()