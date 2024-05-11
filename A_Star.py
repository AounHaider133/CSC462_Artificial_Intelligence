import heapq
import math

#Heuristic
def euclidean_distance(node1, node2):    
    x1, y1 = node1
    x2, y2 = node2
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def a_star_search(graph, start, goal, coordinates):
    open_set = []
    heapq.heappush(open_set, (0 + euclidean_distance(coordinates[start], coordinates[goal]), 0, start, [start]))
    visited = set()

    while open_set:
        _, cost, current, path = heapq.heappop(open_set)
        if current == goal:
            return path

        visited.add(current)
        for neighbor, weight in graph.get(current, {}).items():
            if neighbor in visited:
                continue
            new_cost = cost + weight
            heapq.heappush(open_set, (new_cost + euclidean_distance(coordinates[neighbor], coordinates[goal]), new_cost, neighbor, path + [neighbor]))

    return "No path found."

graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'D': 4, 'E': 2},
    'C': {'F': 5},
    'D': {},
    'E': {'F': 1},
    'F': {}
}
#Location of each individual node
coordinates = {
    'A': (0, 0),
    'B': (1, 1),
    'C': (0, 2),
    'D': (1, 3),
    'E': (2, 2),
    'F': (3, 3)
}
start_node = 'A'
goal_node = 'F'
path = a_star_search(graph, start_node, goal_node, coordinates)
print("Path:", path)
