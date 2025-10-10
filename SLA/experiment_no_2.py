import math
import random

# ----- Distance Calculation -----
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# ----- Total Distance of a Tour -----
def total_distance(path, cities):
    return sum(distance(cities[path[i]], cities[path[(i + 1) % len(path)]]) for i in range(len(path)))

# ----- Generate Neighbor (Swap Two Cities) -----
def get_neighbor(path):
    neighbor = path[:]
    i, j = random.sample(range(len(path)), 2)
    neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
    return neighbor

# ----- Simulated Annealing Algorithm -----
def simulated_annealing(cities, T=10000, Tmin=1, alpha=0.995):
    # Initial random path
    current_path = list(range(len(cities)))
    random.shuffle(current_path)
    best_path = current_path[:]
    
    current_cost = total_distance(current_path, cities)
    best_cost = current_cost
    
    while T > Tmin:
        new_path = get_neighbor(current_path)
        new_cost = total_distance(new_path, cities)
        deltaE = new_cost - current_cost
        
        # Accept new path if it's better OR probabilistically if worse
        if deltaE < 0 or random.random() < math.exp(-deltaE / T):
            current_path = new_path
            current_cost = new_cost
            
            # Update best solution
            if current_cost < best_cost:
                best_path = current_path[:]
                best_cost = current_cost
        
        # Cooling
        T *= alpha
    
    return best_path, best_cost

# ----- Example -----
cities = [(0, 0), (1, 5), (5, 2), (6, 6), (8, 3), (2, 1)]
best_path, best_cost = simulated_annealing(cities)
print("Best Path:", best_path)
print("Shortest Distance:", round(best_cost, 2))
