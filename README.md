# Dijkstra's Algorithm in Python

This repository contains a Python implementation of **Dijkstra's Algorithm** to find the shortest paths from a source node to all other nodes in a weighted, directed graph. The algorithm uses a priority queue for efficient distance calculations and is suitable for graphs with non-negative edge weights.

---

## How It Works

Dijkstra's algorithm calculates the shortest distance from a source node to all other nodes in a graph. It maintains a **priority queue (min-heap)** to explore nodes with the smallest known distance first. The algorithm updates distances for neighboring nodes as it processes the graph, ensuring optimal paths are found.

### Key Features:
- Uses a **min-heap (priority queue)** for efficient distance updates.
- Handles graphs represented as **adjacency lists**.
- Returns:
  - The shortest distances from the source to each node.
  - The shortest path tree (previous nodes in the path).

---

## Graph Representation

The graph is represented as an **adjacency list**, where:
- Each key is a node in the graph.
- The value for each key is a dictionary of neighboring nodes and their respective edge weights.

### Example Graph:
```python
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'C': 2, 'D': 6},
    'C': {'D': 3, 'E': 5},
    'D': {'E': 1},
    'E': {}
}
