import random

def fitness(path):
    # Fitness: inverse of total distance (for demonstration)
    return -sum(abs(path[i] - path[i+1]) for i in range(len(path) - 1))

def get_neighbor(path):
    # Generate a neighbor by swapping two random positions
    neighbor = path[:]
    i, j = random.sample(range(len(path)), 2)
    neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
    return neighbor

def hill_climbing(initial_path, iterations=1000):
    current_path = initial_path
    current_value = fitness(current_path)
    
    for _ in range(iterations):
        neighbor = get_neighbor(current_path)
        neighbor_value = fitness(neighbor)
        
        if neighbor_value > current_value:
            current_path, current_value = neighbor, neighbor_value
    
    return current_path, current_value

# Example: Path of 5 nodes
initial_path = [1, 2, 3, 4, 5]
best_path, best_value = hill_climbing(initial_path)
print("Best Path Found:", best_path)
print("Best Value:", best_value)