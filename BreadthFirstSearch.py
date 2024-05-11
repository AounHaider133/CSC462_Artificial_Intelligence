from collections import deque

def bfs(graph, start, goal):
    visited = set()  # Set to keep track of visited nodes.
    queue = deque([[start]])  # Queue for BFS with path to the current node.

    while queue:
        path = queue.popleft()  # Get the first path from the queue.
        node = path[-1]  # Get the last node from the path.
        
        if node == goal:
            return path  # Return path if goal is reached.
        
        elif node not in visited:
            for adjacent in graph.get(node, []):  # Get neighbours of node.
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)  # Append new path to the queue.
            
            visited.add(node)  # Mark node as visited.

    return "No path found."  # Return this if no path exists.


graph = {
        'A': ['B', 'C'],
        'B': ['E'],
        'C': ['D', 'G'],
        'D': ['C','E','F'],
        'E': ['B','D'],
        'F': []
    }
start_node = 'A'
goal_node = 'G'
print(bfs(graph, start_node, goal_node))