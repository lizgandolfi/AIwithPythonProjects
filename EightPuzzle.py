from search import Problem, astar_search, EightPuzzle 

def manhattan_distance(node):
    """Manhattan distance for 8-puzzle"""
    state = node.state  
    if isinstance(state[0], int):  # Check if state is a flat list
        state = [state[i:i + 3] for i in range(0, len(state), 3)]  # Convert to 2D list

    goal_positions = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    distance = 0
    for i in range(3):
        for j in range(3):
            tile = state[i][j]
            if tile != 0: 
                goal_i, goal_j = divmod(tile, 3)
                distance += abs(i - goal_i) + abs(j - goal_j)
    return distance


def misplaced_tiles(node):
    """Number of misplaced tiles"""
    state = node.state
    if isinstance(state[0], int):  # Check if state is a flat list
        state = [state[i:i + 3] for i in range(0, len(state), 3)]  # Convert to 2D list
    goal = [(0, 1, 2), (3, 4, 5), (6, 7, 8)]
    misplaced = 0
    for i in range(3):
        for j in range(3):
            tile = state[i][j]
            if tile != 0 and tile != goal[i][j]:  
                misplaced += 1
    return misplaced

def n_max_swap(node):
    """N-MaxSwap"""
    state = node.state
    if isinstance(state[0], int):  # Check if state is a flat list
        state = [state[i:i + 3] for i in range(0, len(state), 3)]  # Convert to 2D list
    flat_state = [tile for row in state for tile in row]
    max_swaps = 0
    for i, tile in enumerate(flat_state):
        for j in range(i + 1, len(flat_state)):
            if tile != 0 and flat_state[j] != 0 and tile > flat_state[j]:
                max_swaps += 1
    return max_swaps

def row_column_misplacement(node):
    """Row and column misplacement"""
    state = node.state
    if isinstance(state[0], int):  # Check if state is a flat list
        state = [state[i:i + 3] for i in range(0, len(state), 3)]  # Convert to 2D list
    misplaced = 0
    for i in range(3):
        for j in range(3):
            tile = state[i][j]
            if tile != 0:  
                goal_i, goal_j = divmod(tile, 3)
                if i != goal_i:
                    misplaced += 1
                if j != goal_j:
                    misplaced += 1
    return misplaced


def create_eight_puzzle_problem(initial_state, goal_state):
    problem = EightPuzzle(initial_state)
    problem.goal = goal_state
    return problem

def actions(self, state):
        self.expanded_nodes = 0  # Initialize the attribute to keep track of the number of expanded nodes
        self.expanded_nodes += 1  # Increment the counter whenever actions are generated
        # Define the actions for the 8-puzzle problem
        pass

def h(self, node):
        """ Return the heuristic value for a given state. Default heuristic function used is 
        h(n) = number of misplaced tiles """

        return sum(s != g for (s, g) in zip(node.state, self.goal))

if __name__ == "__main__":
    # Solve the 8-puzzle 
    # The structure of the state is a single tuple with 9 elements, not three tuples with 3 elements each 
    initial_state = (1, 2, 3, 4, 0, 5, 6, 7, 8) 
    goal_state = (0, 1, 2, 3, 4, 5, 6, 7, 8)

    #Heuristics
    heuristics = [
        ("Manhattan Distance", manhattan_distance),
        ("Misplaced Tiles", misplaced_tiles),
        ("n-MaxSwap", n_max_swap),
        ("Row/Column Misplacement", row_column_misplacement)
    ]

    for heuristic_name, heuristic_func in heuristics:
        problem = create_eight_puzzle_problem(initial_state, goal_state)
        node = astar_search(problem, h=heuristic_func)
        heuristic_value = problem.h(node)
        print(f"Heuristic: {heuristic_name}")
        print(f"Solution Path: {node.solution()}")
        print(f"Heuristic Value: {heuristic_value}")
        print(f"Total Cost: {node.path_cost}")
        print("-----")