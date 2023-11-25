# game.py

from player import Player
from maze_generation import generate_maze
from collision import check_collision


class Game:
    def __init__(self, maze_width, maze_height):
        self.maze = generate_maze(maze_width, maze_height)
        start_row, start_col = 0, 0
        self.player = Player(start_row, start_col)

    def run(self):
        while True:
            direction = input("Enter the direction (UP/DOWN/LEFT/RIGHT): ")
            self.player.move(direction)

            if check_collision(self.player, self.maze):
                print("Collision detected. The game is over.")
                break

            self.display_game_state()

            # Add a win condition here
            if self.player_has_won():
                print("Congratulations! You won!")
                break

            # Add additional conditions to end the game if needed

    def display_game_state(self):
        for row in self.maze:
            print(" ".join("X" if cell == 1 else " " for cell in row))
        print("Player position: ({}, {})".format(self.player.row, self.player.col))

    def player_has_won(self):
        # Add logic to check if the player has won
        # For example, if the player reaches a specific position
        return False  # Replace with your win condition
