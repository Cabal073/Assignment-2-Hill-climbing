import random

# Define the function g(x)
def g(x):
    return (0.0051 * x**5) - (0.1367 * x**4) + (1.24 * x**3) - (4.456 * x**2) + (5.66 * x) - 0.287

# Generate state space
state_space = [round(i * 0.5, 1) for i in range(21)]
step = 0.5

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

# --- Part A: Standard Hill-Climbing (Single Run) ---
print("=== Standard Hill-Climbing (1 Run) ===")
std_x, std_val = hill_climbing(g, state_space, step)
print(f"Result: Found max at x = {std_x}, g(x) = {std_val:.4f}")

# --- Part B: Random-Restart Hill-Climbing (20 Runs) ---
print("\n=== Random-Restart Hill-Climbing (20 Runs) ===")
best_rr_x = None
best_rr_val = float('-inf')

# Run 20 times
for i in range(20):
    x, val = hill_climbing(g, state_space, step)
    if val > best_rr_val:
        best_rr_val = val
        best_rr_x = x

print(f"Best of 20 runs: Found max at x = {best_rr_x}, g(x) = {best_rr_val:.4f}")

# --- Part C: Comparison Analysis ---
print("\n--- Comparison Analysis ---")
print(f"Standard Hill-Climbing Result:    g({std_x}) = {std_val:.4f}")
print(f"Random-Restart Hill-Climbing Best: g({best_rr_x}) = {best_rr_val:.4f}")

difference = best_rr_val - std_val
if difference > 0:
    print(f"\nAnalysis: Random-Restart found a BETTER solution by {difference:.4f}.")
    print("This confirms the function has multiple local maxima.")
    print("Standard hill-climbing got stuck in a 'local maximum' (a smaller hill).")
    print("Random-restart tried enough starting points to escape and find the 'global maximum' (the highest hill).")
elif difference == 0:
    print("\nAnalysis: Both found the same result.")
    print("This might mean the single random start happened to be lucky, or the function is simple enough in this area.")
    print("However, with 20 runs, we have much higher confidence in the result.")