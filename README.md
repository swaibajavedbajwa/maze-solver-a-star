# Maze Solver using A* Search Algorithm

## 📌 Project Overview

This project implements a Maze Solver using the A* (A-Star) Search Algorithm.

The program represents a maze as a grid containing a starting point, a goal point, open spaces, and walls. The A* algorithm searches for the shortest path from the start to the goal while avoiding obstacles.

The project also visualizes the maze, explored nodes, and the final shortest path using Matplotlib.

---

## 🎯 Objectives

The main objectives of this project are:

- Represent a maze as a grid.
- Define start and goal nodes.
- Represent walls and obstacles.
- Treat grid positions as nodes.
- Implement the A* Search Algorithm.
- Use a heuristic to guide the search.
- Find the shortest path between the start and goal.
- Handle cases where the goal is unreachable.
- Visualize the search result and final path.

---

## 🧠 A* Search Algorithm

A* is a pathfinding and graph traversal algorithm that finds a shortest path between two nodes.

It uses the following evaluation function:

**f(n) = g(n) + h(n)**

Where:

- **g(n)** = actual cost from the start node to the current node.
- **h(n)** = estimated cost from the current node to the goal.
- **f(n)** = total estimated cost of the path.

The algorithm always considers the node with the lowest estimated total cost.

---

## 📐 Heuristic Function

This project uses the **Manhattan Distance** heuristic.

The formula is:

**h(n) = |x1 - x2| + |y1 - y2|**

Manhattan Distance is suitable for this project because movement is allowed in four directions:

- Up
- Down
- Left
- Right

---

## 🗺️ Maze Representation

The maze is represented using a two-dimensional grid.

The symbols used are:

| Symbol | Meaning |
|--------|---------|
| `S` | Starting Point |
| `G` | Goal Point |
| `#` | Wall / Obstacle |
| `.` | Open Space |

Example:

```text
S . . # . . .
# # . # . # .
. . . . . # .
. # # # . # .
. . . . . . G
