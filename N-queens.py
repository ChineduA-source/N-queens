import random
import time

def generate_random_state(n):
    """
    Generate a random initial state for the N-Queens problem.

    Parameters:
    - n: int, size of the board (number of queens)

    Returns:
    - list, a random initial state represented as a one-dimensional array
      where each index corresponds to a column and the value represents
      the row position of the queen in that column.
    """
    return [random.randint(0, n-1) for _ in range(n)]

def count_attacking_pairs(state):
    """
    Count the number of attacking pairs in the given state.

    Parameters:
    - state: list, current state of the board

    Returns:
    - int, number of attacking pairs in the given state
    """
    n = len(state)
    attacking_pairs = 0
    for i in range(n):
        for j in range(i+1, n):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                attacking_pairs += 1
    return attacking_pairs

def generate_successor_states(state):
    """
    Generate all possible successor states of the given state.

    Parameters:
    - state: list, current state of the board

    Returns:
    - list, a list of successor states
    """
    successors = []
    n = len(state)
    for col in range(n):  # Corrected loop variable to 'col'
        for row in range(n):
            if state[col] != row:
                # Create a copy of the current state and move the queen in the current column to the new row
                successor = list(state)
                successor[col] = row
                successors.append(successor)
    return successors

def random_restart_hill_climbing(n, max_restarts=100):
    """
    Perform random-restart hill climbing to solve the N-Queens problem.

    Parameters:
    - n: int, size of the board (number of queens)
    - max_restarts: int, maximum number of restarts allowed

    Returns:
    - tuple, containing the final board configuration, the number of attacking pairs,
      and the total time required to reach the final state
    """
    total_time = 0
    restarts = 0
    while restarts < max_restarts:
        start_time = time.time()
        current_state = generate_random_state(n)
        current_cost = count_attacking_pairs(current_state)
        while True:
            successor_states = generate_successor_states(current_state)
            best_successor = min(successor_states, key=count_attacking_pairs)
            best_successor_cost = count_attacking_pairs(best_successor)
            if best_successor_cost >= current_cost:
                break
            current_state = best_successor
            current_cost = best_successor_cost
        end_time = time.time()
        total_time += end_time - start_time
        if current_cost == 0:
            return current_state, current_cost, total_time
        restarts += 1
    return None, None, total_time

def first_choice_hill_climbing(n, max_restarts=100):
    """
    Perform first-choice hill climbing with random-restart to solve the N-Queens problem.

    Parameters:
    - n: int, size of the board (number of queens)
    - max_restarts: int, maximum number of restarts allowed

    Returns:
    - tuple, containing the final board configuration, the number of attacking pairs,
      and the total time required to reach the final state
    """
    total_time = 0
    restarts = 0
    while restarts < max_restarts:
        start_time = time.time()
        current_state = generate_random_state(n)
        current_cost = count_attacking_pairs(current_state)
        while True:
            successor_states = generate_successor_states(current_state)
            random.shuffle(successor_states)  # Shuffle to choose a random successor
            for successor in successor_states:
                successor_cost = count_attacking_pairs(successor)
                if successor_cost < current_cost:
                    current_state = successor
                    current_cost = successor_cost
                    break
            else:  # If no better successor found
                break
        end_time = time.time()
        total_time += end_time - start_time
        if current_cost == 0:
            return current_state, current_cost, total_time
        restarts += 1
    return None, None, total_time

# Change the size of the board
n = 8 

# Track time and solutions for ten runs for each algorithm
total_time_random_restart = 0
total_time_first_choice = 0
conflicts_random_restart = 0
conflicts_first_choice = 0

for i in range(10):
    # Random-restart hill climbing
    solution, conflicts, total_time = random_restart_hill_climbing(n)
    if solution:
        print(f"\nRandom-Restart Hill Climbing - Run {i+1}:")
        print("Final Board Configuration:")
        for row in solution:
            board_row = ['.'] * n
            board_row[row] = 'Q'
            print(" ".join(board_row))
        print("Number of Attacking Pairs:", conflicts)
        print("Total Time:", total_time, "seconds")
        total_time_random_restart += total_time
        conflicts_random_restart += conflicts
    else:
        print(f"\nRandom-Restart Hill Climbing - Run {i+1}: Failed to find a solution within the maximum number of restarts.")

    # First-choice hill climbing
    solution, conflicts, total_time = first_choice_hill_climbing(n)
    if solution:
        print(f"\nFirst-Choice Hill Climbing - Run {i+1}:")
        print("Final Board Configuration:")
        for row in solution:
            board_row = ['.'] * n
            board_row[row] = 'Q'
            print(" ".join(board_row))
        print("Number of Attacking Pairs:", conflicts)
        print("Total Time:", total_time, "seconds")
        total_time_first_choice += total_time
        conflicts_first_choice += conflicts
    else:
        print(f"\nFirst-Choice Hill Climbing - Run {i+1}: Failed to find a solution within the maximum number of restarts.")

# Display results
print("\n\nRandom-Restart Hill Climbing:")
print("Average time taken for 10 runs:", total_time_random_restart / 10, "seconds")
print("Average number of attacking pairs in final states:", conflicts_random_restart / 10)

print("\nFirst-Choice Hill Climbing:")
print("Average time taken for 10 runs:", total_time_first_choice / 10, "seconds")
print("Average number of attacking pairs in final states:", conflicts_first_choice / 10)
