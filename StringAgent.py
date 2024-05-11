from collections import deque

class GraphEnvironment:
    def __init__(self, graph):
        self.graph = graph
        self.path_memory = {}

    def is_valid_state_space(self):
        
        return all(isinstance(neighbors, list) for neighbors in self.graph.values())

class Sensor:
    def __init__(self):
        self.start_node = None
        self.end_node = None

    def sense(self, env):
        if env.is_valid_state_space():
            return env
        else:
            return None

class Actuator:
    def __init__(self, action):
        self.action = action

    def act(self, decision, agent):
        self.action(decision, agent)

class Agent:
    def __init__(self):
        self.sensor = Sensor()
        self.actuator = Actuator(self.print_path)
        self.percept_memory = {}

    def bfs(self, env, start, end):
        visited = set()
        queue = deque([[start]])

        while queue:
            path = queue.popleft()
            node = path[-1]

            if node == end:
                return path

            if node not in visited:
                visited.add(node)

                for neighbor in env.graph.get(node, []):
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)

        return None

    def print_path(self, path, agent):
        if path:
            print(f"Path found: {' -> '.join(path)}")
            agent.percept_memory[(path[0], path[-1])] = path
        else:
            print("No path found.")

    def ask_user_for_nodes(self):
        self.sensor.start_node = input("Enter the starting node: ")
        self.sensor.end_node = input("Enter the ending node: ")

    def sense(self, env):
        return self.sensor.sense(env)

    def decide(self, env):
        start, end = self.sensor.start_node, self.sensor.end_node
        if (start, end) in self.percept_memory:
            return self.percept_memory[(start, end)]
        else:
            return self.bfs(env, start, end)

    def act(self, decision):
        self.actuator.act(decision, self)

# Define the graph
graph = {
    'A': ['B', 'F', 'I'],
    'B': ['A', 'C', 'E'],
    'C': ['B', 'D', 'E'],
    'D': ['C', 'G', 'H'],
    'E': ['B', 'C', 'G'],
    'F': ['A', 'G'],
    'G': ['D', 'E', 'F'],
    'H': ['D'],
    'I': ['A']
}

# Create the environment and agent
env = GraphEnvironment(graph)
agent = Agent()

# Main loop
while True:
    agent.ask_user_for_nodes()
    if agent.sense(env):
        decision = agent.decide(env)
        agent.act(decision)
    else:
        print("Invalid state space.")
