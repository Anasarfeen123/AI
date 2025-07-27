# 🧠 Maze Solver AI

This is a Python-based maze solver that supports multiple classic AI pathfinding algorithms, including:

    🧮 Depth-First Search (DFS)

    🛣️ Breadth-First Search (BFS)

    🧭 Greedy Best-First Search

    🚀 A* (A-star) Search

It takes a text file as a maze input and intelligently finds a path from start (A) to goal (B) using the specified algorithm.

---

# 🧩 How It Works

Each algorithm uses a different strategy to explore the maze:
- <b>Algorithm</b>	Strategy
- <b>DFS</b>	Explores deep first, may get lost
- <b>BFS</b>	Explores evenly, guarantees shortest path (if unweighted)
- <b>Greedy</b>	Rushes toward the goal using only a heuristic
- <b>A*</b>	Uses both path cost and heuristic for optimal + efficient paths

All algorithms return the path (if found), and visualize the solution directly in your terminal and as an image.

---

## 📦 Requirements

    Python 3.6+

    Pillow (pip install pillow) for image output

---

## 📂 File Structure
    
    ├── maze.py         # Main program
    ├── maze1.txt       # Example maze
    ├── maze2.txt       # Another test maze
    └── maze.png        # Output image after solving

---

## 🕹️ Usage

    python maze.py maze1.txt bfs

<b>Arguments:</b>

    maze1.txt – the maze input file

    Algorithm to use – dfs, bfs, greedy, or astar

---

## 🧱 Maze Format

Your maze text file should include:

    A — the start position (exactly once)

    B — the goal position (exactly once)

    █ or any non-space char — walls

    Space ( ) — walkable path

Example

A   █ █
█ █   █
█ █ █ B

---

## 🖼️ Output

    Prints the maze with the solution path marked with *

    Saves a maze.png image showing:

        🟥 Start (Red)

        🟩 Goal (Green)

        🌟 Solution Path (Yellow)

        🔴 Explored Nodes (if enabled)

        🧱 Walls (Dark Grey)
---
## 🧠 How the Heuristic Works

    For greedy and astar, Manhattan distance is used:

    h(n) = |x1 - x2| + |y1 - y2|

For astar, the total cost is:

    f(n) = g(n) + h(n)

    where g(n) is the number of steps from start to the current node.
---
## 🛠️ Future Upgrades


Dijkstra’s algorithm

Live GUI animation

Maze generator

---
## 📸 Sample Output
Screenshot to be added
___
## 👾 Author

Made by <b>Anas Arfeen</b>