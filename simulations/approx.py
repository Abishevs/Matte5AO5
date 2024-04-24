import numpy as np

def f(x):
    return (95000) / (x**2 + 10 * x + 16)

def approximate_integral(a, b, dx):
    total_area = 0
    x = a
    while x < b:
        rectangle_area = f(x) * 2 * np.pi * x * dx
        total_area += rectangle_area
        x += dx
    return total_area

if __name__ == "__main__":
    a = 0  
    b = 5
    dx = 0.00001  
    result_1 = approximate_integral(a, b, dx)
    print("Problem (a) 0 - 5km radie:", result_1)

    a = 5
    b = 10
    result_2 = approximate_integral(a, b, dx)
    print("Problem (b) 5 - 10km radie:", result_2)

    a = 0
    b = 10
    result_3 = approximate_integral(a, b, dx)
    print("Directly from 0 - 10km", result_3)

    print("Diffrence 10 km - 5km radie: ", result_3 - result_1)

