# main.py

from game import Game

def main():
    maze_width = 10  # Replace with the desired width of the maze
    maze_height = 10  # Replace with the desired height of the maze
    game = Game(maze_width, maze_height)
    game.run()

if __name__ == "__main__":
    main()
