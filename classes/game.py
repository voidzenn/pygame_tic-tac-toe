class Game:
  def __init__(self):
    self.previous_turn = "circle"
    self.selected_boxes = []

  def set_previous_turn_cross(self):
    self.previous_turn = "cross"

  def set_previous_turn_circle(self):
    self.previous_turn = "circle"

  def add_position(self, position):
    self.selected_boxes.append(position)

  def get_previous_turn(self):
    return self.previous_turn

  def get_selected_boxes(self):
    return self.selected_boxes

  def is_current_turn_circle(self):
    return self.previous_turn == "circle"
