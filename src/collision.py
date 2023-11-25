# collision.py

def check_collision(player, maze):
    """
    Check for collision between the player and walls in the maze.

    Args:
    - player (Player): The player object.
    - maze (list): The matrix representing the maze.

    Returns:
    - bool: True if there is a collision, False otherwise.
    """
    row, col = player.row, player.col

    # Check if the player is within the bounds of the maze
    if 0 <= row < len(maze) and 0 <= col < len(maze[0]):
        # Check if the player is hitting a wall (1) in the maze
        if maze[row][col] == 1:
            return True  # Collision detected

    return False  # No collision
