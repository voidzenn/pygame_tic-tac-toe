class Game:
  def __init__(self):
    self.previous_turn = "circle"

  def set_previous_turn_cross(self):
    self.previous_turn = "cross"

  def set_previous_turn_circle(self):
    self.previous_turn = "circle"

  def get_previous_turn(self):
    return self.previous_turn

  def is_current_turn_circle(self):
    return self.previous_turn == "circle"
