# game.py

from player import Player
from maze_generation import generate_maze
from collision import check_collision

class Game:
    def __init__(self, maze_width, maze_height):
        self.maze = generate_maze(maze_width, maze_height)
        start_row, start_col = 0, 0  # Choose the initial position of the player
        self.player = Player(start_row, start_col)

    def run(self):
        while True:
            # Update the player's state based on user inputs
            direction = input("Enter the direction (UP/DOWN/LEFT/RIGHT): ")
            self.player.move(direction)

            # Check for collision
            if check_collision(self.player, self.maze):
                print("Collision detected. The game is over.")
                break

            # Display the maze with the current player's position
            self.display_game_state()

            # Add conditions to end the game, for example, if the player reaches a goal

    def display_game_state(self):
        # Display logic for the maze with the player's position
        for row in self.maze:
            print(" ".join("X" if cell == 1 else " " for cell in row))
        print("Player position: ({}, {})".format(self.player.row, self.player.col))
