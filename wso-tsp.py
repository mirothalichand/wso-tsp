import random
import numpy as np

def TSP_WSO(distance_matrix, num_wolves, max_iterations):
    num_cities = len(distance_matrix)
    # Initialize the position of the wolves (randomly)
    wolves = [random.sample(range(num_cities), num_cities) for _ in range(num_wolves)]
    fitness = np.array([evaluate_fitness(wolf, distance_matrix) for wolf in wolves])
    best_wolf = np.argmin(fitness)
    best_route = wolves[best_wolf]
    best_distance = fitness[best_wolf]
    for iteration in range(max_iterations):
        alpha = 1 - iteration / max_iterations
        for i in range(num_wolves):
            j = np.random.randint(num_wolves)
            k = np.random.randint(num_wolves)
            while k == j:
                k = np.random.randint(num_wolves)
            new_wolf = wolves[i].copy() # initialize new_wolf as the copy of wolf before mutation operation
            for i in range(len(wolves[i])):
                if random.uniform(0, 1) < alpha:
                    swap = random.randint(0, len(wolves[i]) - 1)
                    new_wolf[i], new_wolf[swap] = new_wolf[swap], new_wolf[i]
            wolves[i] = new_wolf
            fitness[i] = evaluate_fitness(wolves[i], distance_matrix)
            if fitness[i] < best_distance:
                best_wolf = i
                best_route = wolves[i]
                best_distance = fitness[i]
    return best_route, best_distance

def evaluate_fitness(route, distance_matrix):
    distance = 0
    for i in range(len(route)-1):
        distance += distance_matrix[route[i]][route[i+1]]
    distance += distance_matrix[route[-1]][route[0]]
    return distance

# Define the distance matrix
distance_matrix = [[0, 10, 20, 30], [10, 0, 15, 25], [20, 15, 0, 20], [30, 25, 20, 0]]

# Define the number of wolves
num_wolves = 20

# Define the number of iterations
max_iterations = 100

# Solve the TSP using the WSO algorithm
best_route, best_distance = TSP_WSO(distance_matrix, num_wolves, max_iterations)

# Print the best route and best distance
print("Best route:", best_route)
print("Best distance:", best_distance)

