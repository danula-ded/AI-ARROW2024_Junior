import numpy as np
import matplotlib.pyplot as plt

# Define the functions
def func1(x):
    return 4 * x**2 - 15

def func2(x):
    return -5 * x**2

# Create x values from 1 to 1.5
x = np.linspace(1, 1.5, 100)

# Calculate the y values for each function
y1 = func1(x)
y2 = func2(x)

# Plot the functions
plt.figure()
plt.plot(x, y1, label='y=4∗x^2−15')
plt.plot(x, y2, label='y=−5∗x^2')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

# Find the intersection point
coeff = [4, 5]  # Coefficients of the x^2 term (4 and 5 are the coefficients of x^2 in the two functions)
roots = np.roots(coeff)  # Find the roots of the equation 4*x^2 - 5*x^2 = 0

# Take the real part of the root as the intersection point
intersection_point = np.real(roots[0])

# Print the approximate x coordinate of the intersection point rounded to one decimal place
print("Приблизительная координата по оси OX точки пересечения на указанном отрезке составляет около:", round(intersection_point, 1))