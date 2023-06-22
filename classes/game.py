# Winning combination index
# Board is numbered from 0 -> 9
# 0 1 2
# 3 4 5
# 6 7 8
WINNING_COMBINATION = [[0, 1, 2],
                      [3, 4, 5],
                      [6, 7, 8],
                      [0, 3, 6],
                      [1, 4, 7],
                      [2, 5, 8],
                      [0, 4, 8],
                      [6, 4, 2]]

class Game:
  def __init__(self):
    self.previous_turn = "circle"
    self.selected_boxes = []
    self.circle_selection = []
    self.cross_selection = []

  def set_previous_turn_cross(self):
    self.previous_turn = "cross"

  def set_previous_turn_circle(self):
    self.previous_turn = "circle"

  def get_previous_turn(self):
    return self.previous_turn

  def get_selected_boxes(self):
    return self.selected_boxes

  def get_count_selected_boxes(self):
    return len(self.selected_boxes)

  def get_combination(self):
    return WINNING_COMBINATION

  def get_circle_selection(self):
    return self.circle_selection

  def get_cross_selection(self):
    return self.cross_selection

  def add_position(self, position):
    self.selected_boxes.append(position)

  def add_circle_selection(self, index):
    self.circle_selection.append(index)

  def add_cross_selection(self, index):
    self.cross_selection.append(index)

  def is_current_turn_circle(self):
    return self.previous_turn == "circle"

  def check_combination(self, values):
    for combination in WINNING_COMBINATION:
      if all(value in values for value in combination):
        return True
    return False

  def is_circle_won(self):
    return self.check_combination(self.get_circle_selection())

  def is_cross_won(self):
    return self.check_combination(self.get_cross_selection())

  def check_winner(self):
    if self.is_circle_won():
      print("Circle Won")
    elif self.is_cross_won():
      print("Cross Won")
