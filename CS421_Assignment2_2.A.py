import random

# Define the complex function g(x)
def g(x):
    return (0.0051 * x**5) - (0.1367 * x**4) + (1.24 * x**3) - (4.456 * x**2) + (5.66 * x) - 0.287

# Generate state space from 0 to 10 with step size 0.5
state_space = [round(i * 0.5, 1) for i in range(21)]

# Standard hill-climbing function (reused from part 1)
def hill_climbing(func, state_space, step):
    current_x = random.choice(state_space)
    best_val = func(current_x)
    
    while True:
        left = round(current_x - step, 1)
        right = round(current_x + step, 1)
        
        best_neighbor = current_x
        best_neighbor_val = best_val
        
        if left >= 0 and func(left) > best_neighbor_val:
            best_neighbor = left
            best_neighbor_val = func(left)
        if right <= 10 and func(right) > best_neighbor_val:
            best_neighbor = right
            best_neighbor_val = func(right)
        
        if best_neighbor == current_x:
            return current_x, best_val
        
        current_x = best_neighbor
        best_val = best_neighbor_val

# Random-restart hill-climbing (20 restarts)
num_restarts = 20
step = 0.5

best_overall_x = None
best_overall_val = float('-inf')

print(f"Starting {num_restarts} random restarts...\n")

for i in range(num_restarts):
    x, val = hill_climbing(g, state_space, step)
    print(f"Restart {i+1}: Found max at x = {x}, g(x) = {val:.4f}")
    
    if val > best_overall_val:
        best_overall_val = val
        best_overall_x = x

print(f"\n--- FINAL RESULT ---")
print(f"Global maximum found: g({best_overall_x}) = {best_overall_val:.4f}")