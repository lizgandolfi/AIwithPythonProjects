import time
import math
import random
from games4e import alpha_beta_cutoff_search, ConnectFour, MCT_Node

#Set-up for Monte Carlo Tree Search
def select(node):
    """Select a child node with the highest UCB1 value."""
    C = 1.4  
    if not node.children:
        return None  
    return max(node.children, key=lambda n: n.Q / n.N + C * math.sqrt(math.log(node.N) / n.N))

# Backprop function
def backprop(node, result):
    """Backpropagate the result of a simulation up the tree."""
    while node is not None:
        node.N += 1
        node.Q += result
        node = node.parent

# MCTS_expand function
def mcts_expand(node):
    """Expand a node by adding a child node for each possible action."""
    if not node.children:
        for action in node.state.moves:
            child_state = node.state.result(action)
            child_node = MCT_Node(state=child_state, parent=node, move=action)
            node.children.append(child_node)
    return random.choice(node.children) if node.children else None

#Simulate function
def simulate(game, state):
    """Simulate a random playout from the given state."""
    while not game.terminal_test(state):
        state = game.result(state, random.choice(game.actions(state)))
    return game.utility(state, game.to_move(state))

# Monte Carlo Tree Search Wrapper
def monte_carlo_tree_search_wrapper(state, game, time_limit=14.95):
    root = MCT_Node(state=state)
    start_time = time.time()
    
    while time.time() - start_time < time_limit:
        leaf = select(root)
        if leaf is None:  
            continue
        child = mcts_expand(leaf)
        if child is None:  
            continue
        result = simulate(game, child.state)
        backprop(child, result)

    if root.children:
        return max(root.children, key=lambda p: p.N).move
    else:
        return fallback_move(state, game) 

#In case Monte Carlo Tree Search fails
def fallback_move(state, game):
    return random.choice(game.actions(state))

# Alpha-beta search with 15s cutoff
def alpha_beta_cutoff_with_time(state, game, time_limit=14.95):
    start_time = time.time()
    
    def cutoff_test(state, depth):
        return time.time() - start_time >= time_limit

    return alpha_beta_cutoff_search(state, game, cutoff_test=cutoff_test)

# Play a game between alpha-beta and Monte Carlo
def play_game(game, time_limit=14.95, alpha_beta_starts=True):
    state = game.initial  

    while not game.terminal_test(state):
        if alpha_beta_starts:
            start_time = time.time()
            move = alpha_beta_cutoff_with_time(state, game, time_limit)
            elapsed_time = time.time() - start_time
            print(f"Alpha-beta's move: {move} (took {elapsed_time:.2f} seconds)")
        else:
            start_time = time.time()
            move = monte_carlo_tree_search_wrapper(state, game, time_limit)
            elapsed_time = time.time() - start_time
            print(f"Monte Carlo's move: {move} (took {elapsed_time:.2f} seconds)")
        
        state = game.result(state, move)
        alpha_beta_starts = not alpha_beta_starts
    
    return game.utility(state, game.to_move(state))

# Simulate 30 games
def simulate_games(num_games=30, time_limit=14.95):
    game = ConnectFour()
    results = {'alpha_beta': 0, 'monte_carlo': 0, 'draw': 0}

    for i in range(num_games):
        print(f"Playing game {i + 1}...")
        
        #Alternate between alpha-beta and Monte Carlo starting
        if i % 2 == 0:
            result = play_game(game, time_limit, alpha_beta_starts=True)
        else:
            result = play_game(game, time_limit, alpha_beta_starts=False)

        if result > 0:
            results['alpha_beta'] += 1
            print(f"Game {i+1}: Alpha-beta wins!")
        elif result < 0:
            results['monte_carlo'] += 1
            print(f"Game {i+1}: Monte Carlo wins!")
        else:
            results['draw'] += 1
            print(f"Game {i+1}: It's a draw!")

    return results

# Run 30 games and print results
if __name__ == "__main__":
    final_results = simulate_games(30, time_limit=14.95)
    print("Final Results:")
    print(f"Alpha-Beta wins: {final_results['alpha_beta']}")
    print(f"Monte Carlo wins: {final_results['monte_carlo']}")
    print(f"Draws: {final_results['draw']}")
