import random

# Initialize a population of random board configurations
def initialize_population(board_size):
    population = []
    for _ in range(POPULATION_SIZE):
        board = [random.randint(0, board_size - 1) for _ in range(board_size)]
        population.append(board)
    return population

# Calculate fitness of a board configuration (lower is better)
def fitness(board):
    conflicts = 0
    for i in range(len(board)):
        for j in range(i + 1, len(board)):
            if board[i] == board[j] or abs(i - j) == abs(board[i] - board[j]):
                conflicts += 1
    return conflicts

# Select parents for the next generation using tournament selection
def select_parents(population):
    tournament_size = 3
    parents = []
    for _ in range(2):
        tournament = random.sample(population, tournament_size)
        parents.append(min(tournament, key=fitness))
    return parents

# Crossover two parents to create a child
def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child

# Mutate a board configuration by randomly changing one queen's position
def mutate(board, mutation_rate):
    if random.random() < mutation_rate:
        index_to_mutate = random.randint(0, len(board) - 1)
        new_position = random.randint(0, len(board) - 1)
        board[index_to_mutate] = new_position

# Main genetic algorithm loop
def genetic_algorithm(board_size, population_size, mutation_rate, generations):
    population = initialize_population(board_size)
    for generation in range(generations):
        population.sort(key=fitness)
        best_fitness = fitness(population[0])
        if best_fitness == 0:
            print("Solution found in generation:", generation)
            print(population[0])
            return
        new_population = []
        for _ in range(population_size // 2):
            parent1, parent2 = select_parents(population)
            child1 = crossover(parent1, parent2)
            child2 = crossover(parent2, parent1)
            mutate(child1, mutation_rate)
            mutate(child2, mutation_rate)
            new_population.extend([child1, child2])
        population = new_population

    print("No solution found. Best fitness:", best_fitness)

if __name__ == "__main__":
    BOARD_SIZE = int(input("Enter the board size (e.g., 8): "))
    POPULATION_SIZE = int(input("Enter the population size: "))
    MUTATION_RATE = float(input("Enter the mutation rate (0-1): "))
    GENERATIONS = int(input("Enter the number of generations: "))
    
    genetic_algorithm(BOARD_SIZE, POPULATION_SIZE, MUTATION_RATE, GENERATIONS)