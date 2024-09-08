def f(x, y):
    return x*2 + y*2 + 3*x + 4*y + 5
min_x, min_y = float("inf"), float("inf")
min_value = float("inf")
step_size = 0.1
for x in range(-10, 11):
    for y in range(-10, 11):
        value = f(x, y)
        if value < min_value:
            min_value = value
            min_x, min_y = x, y

print(f"Minimum value: {min_value:.6f} at (x, y) = ({min_x:.2f}, {min_y:.2f})")

#OPTIMIZATION: Python code optimization is a way to make your program perform any task more efficiently and quickly with fewer lines of code, less memory, or other resources involved, while producing the right results.
#Types of optimization:	Linear optimization	Non-linear optimization	Constraint optimization	 Unconstraint optimization	Quadratic optimization
