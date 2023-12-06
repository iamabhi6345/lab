import heapq

# Define the N-Puzzle class
class NPuzzle:
    def __init__(self, puzzle, heuristic):
        self.puzzle = puzzle
        self.size = len(puzzle)
        self.heuristic = heuristic
        self.parent = None

    def __lt__(self, other):
        return self.heuristic(self.puzzle) < other.heuristic(other.puzzle)

# Define a heuristic function (e.g., the Manhattan distance)
def manhattan_distance(puzzle):
    goal = [(i, j) for i in range(len(puzzle)) for j in range(len(puzzle))]
    distance = 0
    for i in range(len(puzzle)):
        for j in range(len(puzzle)):
            value = puzzle[i][j]
            if value != 0:
                goal_i, goal_j = goal[value]
                distance += abs(i - goal_i) + abs(j - goal_j)
    return distance

# Define the possible moves
def get_neighbors(puzzle):
    neighbors = []
    size = len(puzzle)
    for i in range(size):
        for j in range(size):
            if puzzle[i][j] == 0:
                if i > 0:
                    neighbor = [list(row) for row in puzzle]
                    neighbor[i][j], neighbor[i - 1][j] = neighbor[i - 1][j], neighbor[i][j]
                    neighbors.append(neighbor)
                if i < size - 1:
                    neighbor = [list(row) for row in puzzle]
                    neighbor[i][j], neighbor[i + 1][j] = neighbor[i + 1][j], neighbor[i][j]
                    neighbors.append(neighbor)
                if j > 0:
                    neighbor = [list(row) for row in puzzle]
                    neighbor[i][j], neighbor[i][j - 1] = neighbor[i][j - 1], neighbor[i][j]
                    neighbors.append(neighbor)
                if j < size - 1:
                    neighbor = [list(row) for row in puzzle]
                    neighbor[i][j], neighbor[i][j + 1] = neighbor[i][j + 1], neighbor[i][j]
                    neighbors.append(neighbor)
    return neighbors

# Greedy Hill Climbing algorithm
def greedy_hill_climbing(initial_state, heuristic):
    start_node = NPuzzle(initial_state, heuristic)
    if heuristic(start_node.puzzle) == 0:
        return [initial_state]
    
    visited = set()
    priority_queue = [start_node]
    
    while priority_queue:
        node = heapq.heappop(priority_queue)
        if heuristic(node.puzzle) == 0:
            path = [node.puzzle]
            while node.parent:
                node = node.parent
                path.append(node.puzzle)
            path.reverse()
            return path
        
        visited.add(tuple(map(tuple, node.puzzle)))
        
        for neighbor in get_neighbors(node.puzzle):
            if tuple(map(tuple, neighbor)) not in visited:
                neighbor_node = NPuzzle(neighbor, heuristic)
                neighbor_node.parent = node
                heapq.heappush(priority_queue, neighbor_node)
    
    return None

# Example usage
if __name__ == '__main__':
    initial_state = [[7, 2, 4], [5, 0, 6], [8, 3, 1]]  # Initial puzzle state
    goal_state = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]      # Goal state

    path = greedy_hill_climbing(initial_state, manhattan_distance)

    if path:
        for state in path:
            print("\n".join(" ".join(str(cell) for cell in row) for row in state))
    else:
        print("No solution found.")
