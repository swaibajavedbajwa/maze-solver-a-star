import heapq
import matplotlib.pyplot as plt


# --------------------------------------------------
# A* SEARCH ALGORITHM
# --------------------------------------------------

def heuristic(node, goal):
    """
    Manhattan Distance heuristic.
    Calculates the estimated distance between
    the current node and the goal node.
    """
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])


def get_neighbors(maze, node):
    """
    Returns all valid neighboring nodes
    (up, down, left, right).
    """
    rows = len(maze)
    cols = len(maze[0])

    row, col = node

    directions = [
        (-1, 0),  # Up
        (1, 0),   # Down
        (0, -1),  # Left
        (0, 1)    # Right
    ]

    neighbors = []

    for dr, dc in directions:
        new_row = row + dr
        new_col = col + dc

        # Check if node is inside the maze
        if 0 <= new_row < rows and 0 <= new_col < cols:

            # '#' represents a wall
            if maze[new_row][new_col] != '#':
                neighbors.append((new_row, new_col))

    return neighbors


def a_star(maze, start, goal):
    """
    Finds the shortest path from start to goal
    using the A* Search Algorithm.
    """

    # Priority queue
    open_set = []

    # f(n) = g(n) + h(n)
    heapq.heappush(open_set, (0, start))

    # Cost from start to each node
    g_score = {start: 0}

    # Stores the previous node
    came_from = {}

    # Keep track of explored nodes
    explored = []

    while open_set:

        # Get node with lowest f(n)
        current_f, current = heapq.heappop(open_set)

        explored.append(current)

        # Goal reached
        if current == goal:
            path = []

            while current in came_from:
                path.append(current)
                current = came_from[current]

            path.append(start)
            path.reverse()

            return path, explored

        # Check neighboring nodes
        for neighbor in get_neighbors(maze, current):

            # Cost of moving to neighboring node
            tentative_g_score = g_score[current] + 1

            # If this route is better
            if (
                neighbor not in g_score
                or tentative_g_score < g_score[neighbor]
            ):

                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score

                # Manhattan heuristic
                h_score = heuristic(neighbor, goal)

                # f(n) = g(n) + h(n)
                f_score = tentative_g_score + h_score

                heapq.heappush(
                    open_set,
                    (f_score, neighbor)
                )

    # No path exists
    return None, explored


# --------------------------------------------------
# VISUALIZATION
# --------------------------------------------------

def visualize_maze(maze, start, goal, path, explored):
    """
    Displays the maze, explored nodes and final path.
    """

    rows = len(maze)
    cols = len(maze[0])

    # Create numeric grid
    grid = []

    for row in range(rows):
        grid_row = []

        for col in range(cols):

            if maze[row][col] == '#':
                grid_row.append(0)       # Wall

            elif (row, col) in path if path else False:
                grid_row.append(3)       # Final path

            elif (row, col) in explored:
                grid_row.append(2)       # Explored

            else:
                grid_row.append(1)       # Empty

        grid.append(grid_row)

    plt.figure(figsize=(8, 6))

    plt.imshow(grid)

    # Mark start and goal
    plt.scatter(
        start[1],
        start[0],
        marker='o',
        s=150,
        label='Start'
    )

    plt.scatter(
        goal[1],
        goal[0],
        marker='X',
        s=150,
        label='Goal'
    )

    # Draw path
    if path:
        path_rows = [node[0] for node in path]
        path_cols = [node[1] for node in path]

        plt.plot(
            path_cols,
            path_rows,
            linewidth=3,
            label='Shortest Path'
        )

    plt.title("Maze Solver using A* Search")

    plt.xticks(range(cols))
    plt.yticks(range(rows))

    plt.grid(True)

    plt.legend()

    plt.show()


# --------------------------------------------------
# MAIN PROGRAM
# --------------------------------------------------

def main():

    # Maze representation
    # S = Start
    # G = Goal
    # # = Wall
    # . = Empty space

    maze = [
        ['S', '.', '.', '#', '.', '.', '.'],
        ['#', '#', '.', '#', '.', '#', '.'],
        ['.', '.', '.', '.', '.', '#', '.'],
        ['.', '#', '#', '#', '.', '#', '.'],
        ['.', '.', '.', '.', '.', '.', 'G']
    ]

    # Find Start and Goal
    start = None
    goal = None

    for row in range(len(maze)):
        for col in range(len(maze[0])):

            if maze[row][col] == 'S':
                start = (row, col)

            elif maze[row][col] == 'G':
                goal = (row, col)

    # Run A* Search
    path, explored = a_star(maze, start, goal)

    # Display result
    print("\n===================================")
    print("      A* MAZE SOLVER")
    print("===================================")

    print("Start:", start)
    print("Goal:", goal)

    print("Explored Nodes:", len(explored))

    if path:

        print("Path Found!")

        print("Shortest Path Length:", len(path) - 1)

        print("\nShortest Path:")

        for node in path:
            print(node, end=" -> ")

        print("\n")

    else:

        print("No path found!")
        print("The goal is unreachable from the start.")

    # Visualize result
    visualize_maze(
        maze,
        start,
        goal,
        path,
        explored
    )


# Run the program
if __name__ == "__main__":
    main()
