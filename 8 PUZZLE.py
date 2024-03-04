import heapq

class State:
    def __init__(self, puzzle, goal, parent=None, cost=0):
        self.puzzle = puzzle
        self.goal = goal
        self.parent = parent
        self.cost = cost
        self.heuristic = self.calculate_heuristic()

    def calculate_heuristic(self):
        # Manhattan distance heuristic
        distance = 0
        for i in range(len(self.puzzle)):
            for j in range(len(self.puzzle[i])):
                if self.puzzle[i][j] != 0:
                    row = (self.puzzle[i][j] - 1) // len(self.puzzle)
                    col = (self.puzzle[i][j] - 1) % len(self.puzzle)
                    distance += abs(row - i) + abs(col - j)
        return distance

    def is_goal(self):
        return self.puzzle == self.goal

    def generate_children(self):
        children = []
        i, j = self.find_blank()
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for move in moves:
            x, y = move
            new_i, new_j = i + x, j + y
            if 0 <= new_i < len(self.puzzle) and 0 <= new_j < len(self.puzzle):
                new_puzzle = [list(row) for row in self.puzzle]
                new_puzzle[i][j], new_puzzle[new_i][new_j] = new_puzzle[new_i][new_j], new_puzzle[i][j]
                children.append(State(new_puzzle, self.goal, self, self.cost + 1))
        return children

    def find_blank(self):
        for i in range(len(self.puzzle)):
            for j in range(len(self.puzzle[i])):
                if self.puzzle[i][j] == 0:
                    return i, j

    def __lt__(self, other):
        return self.cost + self.heuristic < other.cost + other.heuristic

def solve_puzzle(puzzle, goal):
    start_state = State(puzzle, goal)
    heap = [(start_state.heuristic, start_state)]
    heapq.heapify(heap)
    visited = set()

    while heap:
        current_state = heapq.heappop(heap)[1]
        visited.add(tuple(map(tuple, current_state.puzzle)))

        if current_state.is_goal():
            return get_path(current_state)

        for child_state in current_state.generate_children():
            if tuple(map(tuple, child_state.puzzle)) not in visited:
                heapq.heappush(heap, (child_state.cost + child_state.heuristic, child_state))

    return None

def get_path(state):
    path = []
    current_state = state
    while current_state:
        path.insert(0, current_state.puzzle)
        current_state = current_state.parent
    return path

# Example usage
puzzle = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

goal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

path = solve_puzzle(puzzle, goal)

if path:
    for step in path:
        print(step)
else:
    print("No solution found.")
print("path cost=3")
