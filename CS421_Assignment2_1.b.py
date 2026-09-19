import random

# Define the function f(x) = 2 - x^2
def f(x):
    return 2 - x**2

# Generate discrete state space from -5 to 5 with step size 0.5
state_space = [round(-5 + i * 0.01, 2) for i in range(21)]

# Pick a random starting point
current_x = random.choice(state_space)
print(f"Starting at x = {current_x}, f(x) = {f(current_x)}")

# Hill-climbing loop
step = 0.01
while True:
    # Check left and right neighbors
    left = round(current_x - step, 1)
    right = round(current_x + step, 1)

    best_x = current_x
    best_val = f(current_x)

    if left >= -5 and f(left) > best_val:
        best_x = left
        best_val = f(left)
    if right <= 5 and f(right) > best_val:
        best_x = right
        best_val = f(right)

    # If no better neighbor, we're done
    if best_x == current_x:
        break

    current_x = best_x

print(f"\nMaximum found: f({current_x}) = {f(current_x)}")