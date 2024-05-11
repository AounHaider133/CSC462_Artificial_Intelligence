import heapq

# Grid parameters and barriers
dimension = 9
barriers = {(0, 3), (0, 4), (0, 8), (1, 6), (2, 3), (2, 4), (3, 0), (3, 1), (3, 3), (3, 8), (4, 1), (4, 3), (4, 5), (4, 8), (5, 3), (5, 5), (5, 6), (6, 0), (6, 7), (7, 0), (7, 1), (7, 2), (7, 5), (8, 0)}
target = (8, 8)  # Adjusted goal state to fit within the 9x9 grid

# Starting coordinate
origin = (0, 0)

# Calculate Manhattan distance
def calculate_manhattan(coord, target):
    return abs(coord[0] - target[0]) + abs(coord[1] - target[1])

# Greedy algorithm using Manhattan distance
def greedy_path_finding(origin, target, barriers, dimension):
    priority_queue = [(calculate_manhattan(origin, target), origin)]
    seen = set()
    path_length = 0
    limit = 200

    while priority_queue and path_length < limit:
        _, coord = heapq.heappop(priority_queue)
        print(f"Agent is at: {coord}")
        path_length += 1

        if coord == target:
            print(f"Target reached in {path_length} moves.")
            return

        seen.add(coord)
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
        for move in moves:
            next_coord = (coord[0] + move[0], coord[1] + move[1])
            if 0 <= next_coord[0] < dimension and 0 <= next_coord[1] < dimension and next_coord not in barriers and next_coord not in seen:
                heapq.heappush(priority_queue, (calculate_manhattan(next_coord, target), next_coord))

    print(f"Limit of {limit} moves reached without finding the target.")

# Execute the path finding
greedy_path_finding(origin, target, barriers, dimension)
