# player.py

class Player:
    def __init__(self):
        # Initialize player attributes here
        pass

    def move(self, direction):
        # Player movement logic
        pass
class Player:
    def __init__(self, start_row, start_col):
        self.row = start_row
        self.col = start_col

    def move(self, direction):
        if direction == "UP":
            self.row -= 1
        elif direction == "DOWN":
            self.row += 1
        elif direction == "LEFT":
            self.col -= 1
        elif direction == "RIGHT":
            self.col += 1
