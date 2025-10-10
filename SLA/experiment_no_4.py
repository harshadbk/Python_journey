import math
import random

# ----- Distance Function -----
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# ----- Total Path Cost -----
def path_cost(path, cities):
    return sum(distance(cities[path[i]], cities[path[(i + 1) % len(path)]]) for i in range(len(path)))

# ----- Node Structure for MCTS -----
class Node:
    def __init__(self, path, unvisited, parent=None):
        self.path = path                # Current path (partial solution)
        self.unvisited = unvisited      # Remaining cities
        self.parent = parent
        self.children = []
        self.visits = 0
        self.reward = 0.0

    def is_fully_expanded(self):
        return len(self.unvisited) == 0 or len(self.children) == len(self.unvisited)

# ----- MCTS Components -----
def uct_value(total_visits, node_visits, node_reward, c=1.41):
    if node_visits == 0:
        return float('inf')
    return (node_reward / node_visits) + c * math.sqrt(math.log(total_visits) / node_visits)

def select_node(node):
    while node.children:
        node = max(node.children, key=lambda n: uct_value(node.visits, n.visits, n.reward))
    return node

def expand_node(node, cities):
    if not node.unvisited:
        return node
    city = random.choice(node.unvisited)
    new_path = node.path + [city]
    new_unvisited = node.unvisited.copy()
    new_unvisited.remove(city)
    child = Node(new_path, new_unvisited, parent=node)
    node.children.append(child)
    return child

def simulate(node, cities):
    # Randomly complete the tour
    current_path = node.path[:]
    remaining = node.unvisited[:]
    random.shuffle(remaining)
    current_path += remaining
    cost = path_cost(current_path, cities)
    # Lower cost → higher reward
    return 1 / cost

def backpropagate(node, reward):
    while node:
        node.visits += 1
        node.reward += reward
        node = node.parent

# ----- Monte Carlo Tree Search -----
def mcts_tsp(cities, iterations=5000):
    n = len(cities)
    root = Node([], list(range(n)))

    for _ in range(iterations):
        node = select_node(root)
        if not node.is_fully_expanded():
            node = expand_node(node, cities)
        reward = simulate(node, cities)
        backpropagate(node, reward)

    # Best child (highest reward)
    best_child = max(root.children, key=lambda n: n.reward / n.visits if n.visits > 0 else 0)
    # Complete path by random shuffle for remaining cities
    best_path = best_child.path + random.sample(best_child.unvisited, len(best_child.unvisited))
    best_cost = path_cost(best_path, cities)
    return best_path, best_cost

# ----- Example -----
cities = [(0,0), (1,5), (5,2), (6,6), (8,3), (2,1)]
best_path, best_cost = mcts_tsp(cities, iterations=3000)
print("Best Path Found:", best_path)
print("Shortest Distance (approx):", round(best_cost, 2))
