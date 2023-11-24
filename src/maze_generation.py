# src/maze_generation.py

import random

def generate_maze(width, height):
    """
    Generates a maze using the Recursive Backtracking algorithm.

    Args:
    - width (int): Width of the maze.
    - height (int): Height of the maze.

    Returns:
    - list: A matrix representing the generated maze.
    """
    maze = [[1] * width for _ in range(height)]

    start_column = random.randint(0, width - 1)
    maze[0][start_column] = 0

    recursive_backtracking(maze, 0, start_column)

    return maze

def recursive_backtracking(maze, row, column):
    """
    Recursive function for Recursive Backtracking.

    Args:
    - maze (list): Matrix representing the maze.
    - row (int): Current row.
    - column (int): Current column.
    """
    directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]
    random.shuffle(directions)

    for dr, dc in directions:
        new_row, new_column = row + dr, column + dc
        if 0 <= new_row < len(maze) and 0 <= new_column < len(maze[0]) and maze[new_row][new_column] == 1:
            maze[row + dr // 2][column + dc // 2] = 0
            maze[new_row][new_column] = 0
            recursive_backtracking(maze, new_row, new_column)

# Example of usage
if __name__ == "__main__":
    maze_width = 11
    maze_height = 11
    generated_maze = generate_maze(maze_width, maze_height)

    for row in generated_maze:
        print(" ".join("X" if cell == 1 else " " for cell in row))
